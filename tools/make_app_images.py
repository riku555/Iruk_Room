#!/usr/bin/env python3
"""アプリアイコン(正方形PNG)から、サイト用の2枚を生成する。

- images/<slug>-icon.png  : 512x512。アイコンをLANCZOSで縮小（正方形のまま。角丸はCSS任せ）。
- images/<slug>-thumb.png : 640x400(16:10)。テーマ色の縦グラデ背景に、
                            角丸(半径58・4倍マスクで滑らか)＋ソフト影を付けたアイコン(260px)を中央配置。

使い方:
  python tools/make_app_images.py --src <icon.png> --slug <slug> [--top RRGGBB --bottom RRGGBB]
"""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

THUMB_W, THUMB_H = 640, 400
ICON_OUT = 512
ICON_IN_THUMB = 260
RADIUS = 58
SS = 4  # マスクのスーパーサンプリング倍率


def hex_to_rgb(s: str):
    s = s.lstrip("#")
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


def vertical_gradient(w, h, top, bottom):
    base = Image.new("RGB", (w, h), top)
    top_r, top_g, top_b = top
    bot_r, bot_g, bot_b = bottom
    for y in range(h):
        t = y / (h - 1)
        r = round(top_r + (bot_r - top_r) * t)
        g = round(top_g + (bot_g - top_g) * t)
        b = round(top_b + (bot_b - top_b) * t)
        for x in range(w):
            base.putpixel((x, y), (r, g, b))
    return base


def rounded_icon(src_img, size, radius, ss):
    """角丸マスクを掛けたアイコン(RGBA, size×size)を返す。マスクはss倍で作って縮小し滑らかに。"""
    icon = src_img.convert("RGBA").resize((size, size), Image.LANCZOS)
    mask_big = Image.new("L", (size * ss, size * ss), 0)
    d = ImageDraw.Draw(mask_big)
    d.rounded_rectangle([0, 0, size * ss - 1, size * ss - 1], radius=radius * ss, fill=255)
    mask = mask_big.resize((size, size), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(icon, (0, 0), mask)
    return out, mask


def make_thumb(src_img, top, bottom):
    bg = vertical_gradient(THUMB_W, THUMB_H, top, bottom).convert("RGBA")
    icon, mask = rounded_icon(src_img, ICON_IN_THUMB, RADIUS, SS)
    x = (THUMB_W - ICON_IN_THUMB) // 2
    y = (THUMB_H - ICON_IN_THUMB) // 2

    # ソフト影: 角丸シルエットを少し下にずらしてぼかす
    shadow = Image.new("RGBA", (THUMB_W, THUMB_H), (0, 0, 0, 0))
    silhouette = Image.new("RGBA", (ICON_IN_THUMB, ICON_IN_THUMB), (20, 30, 55, 150))
    shadow.paste(silhouette, (x, y + 14), mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))

    out = Image.alpha_composite(bg, shadow)
    out.alpha_composite(icon, (x, y))
    return out.convert("RGB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="元アイコンPNG（正方形・1024推奨）")
    ap.add_argument("--slug", required=True, help="出力ファイル名の接頭辞（例: block-puzzle）")
    ap.add_argument("--top", default="DDF3FF", help="サムネ背景・上端色 RRGGBB")
    ap.add_argument("--bottom", default="E3E9FF", help="サムネ背景・下端色 RRGGBB")
    args = ap.parse_args()

    src = Image.open(args.src)
    IMAGES.mkdir(exist_ok=True)

    icon_out = IMAGES / f"{args.slug}-icon.png"
    src.convert("RGBA").resize((ICON_OUT, ICON_OUT), Image.LANCZOS).save(icon_out)

    thumb_out = IMAGES / f"{args.slug}-thumb.png"
    make_thumb(src, hex_to_rgb(args.top), hex_to_rgb(args.bottom)).save(thumb_out)

    print(f"wrote {icon_out} (512x512)")
    print(f"wrote {thumb_out} (640x400)")


if __name__ == "__main__":
    main()
