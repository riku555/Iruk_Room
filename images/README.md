# 必要な画像一覧

このフォルダに以下の画像を入れると、プレースホルダーが実際の画像に置き換わります。
（ファイル名はHTML内の指定に合わせています。変更する場合はHTML側も直してください）

## 共通・トップページ
| ファイル名 | 用途 | 推奨サイズ | 形式 |
|---|---|---|---|
| `iruk-avatar.png` | トップのプロフィール画像 | 600 × 600px（正方形） | PNG / JPG |
| `favicon.png` | ブラウザタブのアイコン（任意） | 512 × 512px | PNG |

## アプリ一覧・トップのサムネイル（16:10 推奨）
| ファイル名 | アプリ |
|---|---|
| `national-flag-quest-thumb.png` | あおくんの国旗クエスト |
| `block-puzzle-thumb.png` | あおくんのブロックパズル（★配置済み・`tools/make_app_images.py`で生成） |
| `word-puzzle-thumb.png` | あおくんの英単語パズル（★配置済み・`tools/make_app_images.py`で生成） |
| `license-museum-thumb.png` | あおくんの資格博物館（★配置済み・`tools/make_app_images.py`で生成） |
| `board-game-thumb.png` | あおくんのゲーム工房・開発中 |
| `classical-music-quest-thumb.png` | あおくんの音楽クエスト（★配置済み・`tools/make_app_images.py`で生成） |
| `bond-bond-thumb.png` | Bond Bond!（元素結合ボードゲーム・★配置済み・`tools/make_app_images.py`で生成） |
| `bear-trail-thumb.png` | ベア・トレイル（★配置済み・`tools/make_app_images.py`で生成） |
| `tower-defender-thumb.png` | Tower Defender |
| `subsclens-thumb.png` | SubscLens |
| `heartsound-thumb.png` | 赤ちゃんの心音＆妊娠記録（★配置済み・`tools/make_app_images.py`で生成） |

推奨サイズ：640 × 400px 程度

## アプリ詳細ページ（例：ベア・トレイル）
| ファイル名 | 用途 | 推奨サイズ |
|---|---|---|
| `bear-trail-icon.png` | アプリアイコン（★配置済み 512×512・`tools/make_app_images.py`で生成） | 512 × 512px（正方形） |
| `bear-trail-1.png`〜`bear-trail-4.png` | スクリーンショット（未配置・開発中） | 縦向き（例 1170 × 2532px） |
| `board-game-icon.png` | アプリアイコン（あおくんのゲーム工房・未配置） | 512 × 512px（正方形） |
| `board-game-1.png`〜`board-game-4.png` | スクリーンショット（あおくんのゲーム工房・未配置） | 縦向き（例 1170 × 2532px） |
| `bond-bond-icon.png` | アプリアイコン（Bond Bond!・★配置済み 512×512・`tools/make_app_images.py`で生成） | 512 × 512px（正方形） |
| `bond-bond-1.png`〜`bond-bond-4.png` | スクリーンショット（Bond Bond!・未配置・開発中） | 縦向き（例 1170 × 2532px） |
| `national-flag-quest-icon.png` | アプリアイコン（あおくんの国旗クエスト） | 512 × 512px（正方形） |
| `national-flag-quest-1.png`〜`national-flag-quest-4.png` | スクリーンショット（あおくんの国旗クエスト） | 縦向き（例 1170 × 2532px） |
| `block-puzzle-icon.png` | アプリアイコン（あおくんのブロックパズル・配置済み 512×512） | 512 × 512px（正方形） |
| `block-puzzle-1.jpg`〜`block-puzzle-5.jpg` | スクリーンショット（あおくんのブロックパズル・★配置済み 640幅JPEG・`tools/fetch_store_screenshots.py`で取得） | 縦向き |
| `word-puzzle-icon.png` | アプリアイコン（あおくんの英単語パズル・配置済み 512×512） | 512 × 512px（正方形） |
| `word-puzzle-1.png`〜`word-puzzle-4.png` | スクリーンショット（あおくんの英単語パズル・未配置） | 縦向き（例 1170 × 2532px） |
| `license-museum-icon.png` | アプリアイコン（あおくんの資格博物館・配置済み 512×512） | 512 × 512px（正方形） |
| `license-museum-1.png`〜`license-museum-4.png` | スクリーンショット（あおくんの資格博物館・未配置） | 縦向き（例 1170 × 2532px） |
| `heartsound-icon.png` | アプリアイコン（赤ちゃんの心音＆妊娠記録・配置済み 512×512） | 512 × 512px（正方形） |
| `heartsound-1.png`〜`heartsound-4.png` | スクリーンショット（赤ちゃんの心音＆妊娠記録・未配置） | 縦向き（例 1170 × 2532px） |
| `classical-music-quest-icon.png` | アプリアイコン（あおくんの音楽クエスト・★配置済み 512×512・`tools/make_app_images.py`で生成） | 512 × 512px（正方形） |
| `classical-music-quest-1.png`〜`classical-music-quest-4.png` | スクリーンショット（あおくんの音楽クエスト・未配置・開発中） | 縦向き（例 1170 × 2532px） |

> `block-puzzle-icon.png` / `-thumb.png` は `tools/make_app_images.py` でアプリアイコンから生成しています（他アプリも同スクリプトで統一可能）。

他のアプリの詳細ページを作るときも、同じ命名ルール（`アプリ名-icon.png` / `アプリ名-1.jpg`…）で用意すると分かりやすいです。

## スクリプトで画像を用意する

`tools/` に2つの生成スクリプトがあります（Python + Pillow が必要: `pip install pillow`）。

### 1. アイコン・サムネの生成 — `make_app_images.py`
アプリアイコン（正方形PNG）から、サイト用の `-icon.png`（512²）と `-thumb.png`（640×400・淡色グラデ背景に中央配置）を生成。
```bash
python tools/make_app_images.py --src <icon.png> --slug <slug> --top FBF4E4 --bottom F1E4C6
```

### 2. App Store スクショの取得 — `fetch_store_screenshots.py`
**配信中アプリ**の App Store 商品ページから公開スクショを取得し、Web用に軽量化（幅640・JPEG）して `images/<slug>-N.jpg` に保存。自分のアプリのスクショなので権利上も問題なし。
```bash
# まずURLだけ確認（--dry-run）
python tools/fetch_store_screenshots.py --id <AppStore数値ID> --slug <slug> --dry-run
# 取得して配置（例: ブロックパズル）
python tools/fetch_store_screenshots.py --id 6777042903 --slug block-puzzle
```
主なオプション: `--max N`（枚数制限）/ `--device pad`（iPad版）/ `--width 640` / `--country jp`。
実行後に表示される `<div class="shot"><img …></div>` を、詳細ページ `apps/<slug>.html` のスクショ欄に貼れば完成。

配信中アプリの App Store 数値ID（`apps.apple.com/jp/app/idXXXXXXXXXX` の数字）。**開発者(RIKU KAKIZOE, artistId 6775458025)の配信中8アプリすべてスクショ取得・詳細ページ適用済み（2026-07-23）**:

| アプリ | slug | ID | スクショ |
|---|---|---|---|
| あおくんのブロックパズル | block-puzzle | 6777042903 | ★5枚 |
| あおくんの英単語パズル | word-puzzle | 6778866021 | ★6枚 |
| あおくんの国旗クエスト | national-flag-quest | 6780043491 | ★6枚 |
| あおくんの資格博物館 | license-museum | 6780581953 | ★6枚 |
| あおくんの音楽クエスト | classical-music-quest | 6781711066 | ★6枚 |
| Bond Bond! | bond-bond | 6789931687 | ★6枚 |
| ベア・トレイル | bear-trail | 6785072315 | ★4枚（縦のみ） |
| SubscLens | subsclens | 6787697501 | ★5枚 |

> スクショは縦向き（`--orientation portrait`）・最大6枚（`--max 6`）で取得。ベア・トレイル/資格博物館は横向きスクショも持つが、サイトの縦型枠に合わせ縦向きのみ採用している。
> 開発者の全アプリIDは `python -c "import json,urllib.request as u; print(u.urlopen('https://itunes.apple.com/lookup?id=6775458025&entity=software&country=jp&limit=200').read().decode())"` で一覧取得できる。

---

### 画像がまだ無い場合
画像を入れなくてもサイト自体は正しく表示されます（グレーの枠にファイル名が表示されるだけ）。
画像が用意でき次第、このフォルダに置いてください。
