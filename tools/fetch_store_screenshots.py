#!/usr/bin/env python3
"""App Store の商品ページから、公開スクリーンショットを取得してサイト用に配置する。

自分が公開したアプリのスクリーンショットを、App Store の商品ページ埋め込みデータ
(serialized-server-data) から取得し、Web 用に軽量化して images/<slug>-N.jpg に保存する。

- まず iTunes Lookup API を試し、screenshotUrls が空なら商品ページHTMLから抽出する
  （新しめのアプリは Lookup API がスクショを返さないことがあるため）。
- iPhone(phone) と iPad(pad) を選べる。既定は phone。
- 取得後、幅を縮小して JPEG(progressive) で保存（詳細ページのスクショ欄に最適）。

使い方:
  python tools/fetch_store_screenshots.py --id 6777042903 --slug block-puzzle
  python tools/fetch_store_screenshots.py --id 6777042903 --slug block-puzzle --max 5 --width 640
  python tools/fetch_store_screenshots.py --id 6777042903 --slug block-puzzle --dry-run   # URL一覧だけ表示

出力後、詳細ページ apps/<slug>.html のスクショ欄を次の形にすると表示される:
  <div class="shot"><img src="../images/<slug>-1.jpg" alt="..." loading="lazy" /></div>
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/17.0 Safari/605.1.15")


def http_get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def build_url(shot: dict, fmt: str = "png") -> str:
    """screenshot ノード(template + width/height)から実URLを組み立てる。"""
    t = shot["template"]
    w, h = shot.get("width", 0), shot.get("height", 0)
    return (t.replace("{w}", str(w)).replace("{h}", str(h))
             .replace("{c}", "bb").replace("{f}", fmt))


def _find_shelf_items(node, device_key: str, acc: list):
    """serialized-server-data を再帰的に辿り、product_media_<device>_ の items を集める。"""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == device_key and isinstance(v, dict) and isinstance(v.get("items"), list):
                acc.append(v["items"])
            _find_shelf_items(v, device_key, acc)
    elif isinstance(node, list):
        for v in node:
            _find_shelf_items(v, device_key, acc)


def _find_any_screenshots(node, acc: list):
    """フォールバック: template を持つ screenshot ノードを再帰的にすべて集める。"""
    if isinstance(node, dict):
        if "screenshot" in node and isinstance(node["screenshot"], dict) \
                and "template" in node["screenshot"]:
            acc.append(node["screenshot"])
        for v in node.values():
            _find_any_screenshots(v, acc)
    elif isinstance(node, list):
        for v in node:
            _find_any_screenshots(v, acc)


def screenshots_from_page(app_id: str, country: str, device: str) -> list:
    """商品ページHTMLの serialized-server-data からスクショURLを抽出。"""
    url = f"https://apps.apple.com/{country}/app/id{app_id}"
    html = http_get(url).decode("utf-8", "replace")
    m = re.search(r'<script[^>]*id="serialized-server-data"[^>]*>(.*?)</script>',
                  html, re.S)
    if not m:
        return []
    data = json.loads(m.group(1))

    device_key = "product_media_pad_" if device == "pad" else "product_media_phone_"
    groups: list = []
    _find_shelf_items(data, device_key, groups)

    shots = []
    for items in groups:
        for it in items:
            s = it.get("screenshot")
            if isinstance(s, dict) and "template" in s:
                shots.append(s)
    if shots:
        return shots

    # フォールバック（device 指定は効かないが、少なくとも取得はできる）
    _find_any_screenshots(data, shots)
    return shots


def screenshots_from_lookup(app_id: str, country: str, device: str) -> list:
    """iTunes Lookup API。screenshotUrls があれば使う（無ければ空）。"""
    url = f"https://itunes.apple.com/lookup?id={app_id}&country={country}"
    data = json.loads(http_get(url).decode("utf-8", "replace"))
    if not data.get("resultCount"):
        return []
    r = data["results"][0]
    key = "ipadScreenshotUrls" if device == "pad" else "screenshotUrls"
    # Lookup のURLは実URL（テンプレではない）なので疑似ノード化
    return [{"_direct": u} for u in r.get(key, [])]


def resolve_url(shot: dict) -> str:
    return shot["_direct"] if "_direct" in shot else build_url(shot)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True, help="App Store の数値ID（例: 6777042903）")
    ap.add_argument("--slug", required=True, help="出力ファイル接頭辞（例: block-puzzle）")
    ap.add_argument("--country", default="jp", help="ストア地域（既定: jp）")
    ap.add_argument("--device", default="phone", choices=["phone", "pad"],
                    help="端末（既定: phone）")
    ap.add_argument("--width", type=int, default=640, help="保存幅px（既定: 640）")
    ap.add_argument("--quality", type=int, default=87, help="JPEG品質（既定: 87）")
    ap.add_argument("--max", type=int, default=0, help="最大枚数（0=全部）")
    ap.add_argument("--start", type=int, default=1, help="出力の開始番号（既定: 1）")
    ap.add_argument("--dry-run", action="store_true", help="URL一覧を表示するだけ")
    args = ap.parse_args()

    # 1) Lookup API → 空なら 2) 商品ページHTML
    shots = screenshots_from_lookup(args.id, args.country, args.device)
    source = "lookup-api"
    if not shots:
        shots = screenshots_from_page(args.id, args.country, args.device)
        source = "product-page"

    if not shots:
        print("スクリーンショットを取得できませんでした。IDと地域(--country)を確認してください。",
              file=sys.stderr)
        return 1

    if args.max > 0:
        shots = shots[:args.max]

    print(f"取得元: {source} / device={args.device} / {len(shots)}枚")
    urls = [resolve_url(s) for s in shots]
    for i, u in enumerate(urls, args.start):
        print(f"  [{i}] {u}")
    if args.dry_run:
        return 0

    IMAGES.mkdir(exist_ok=True)
    import io
    for i, u in enumerate(urls, args.start):
        raw = http_get(u)
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        w, h = im.size
        if w > args.width:
            im = im.resize((args.width, round(h * args.width / w)), Image.LANCZOS)
        out = IMAGES / f"{args.slug}-{i}.jpg"
        im.save(out, "JPEG", quality=args.quality, optimize=True, progressive=True)
        print(f"  wrote {out.relative_to(ROOT)}  {im.size[0]}x{im.size[1]}  "
              f"{out.stat().st_size // 1024}KB")

    print(f"\n完了。詳細ページ apps/{args.slug}.html のスクショ欄を次の形にしてください:")
    for i in range(args.start, args.start + len(urls)):
        print(f'  <div class="shot"><img src="../images/{args.slug}-{i}.jpg" '
              f'alt="{args.slug} スクリーンショット{i}" loading="lazy" /></div>')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
