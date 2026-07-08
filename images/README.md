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
| `bear-trail-thumb.png` | ベア・トレイル |
| `tower-defender-thumb.png` | Tower Defender |
| `subsclens-thumb.png` | SubscLens |
| `heartsound-thumb.png` | 赤ちゃんの心音＆妊娠記録 |

推奨サイズ：640 × 400px 程度

## アプリ詳細ページ（例：ベア・トレイル）
| ファイル名 | 用途 | 推奨サイズ |
|---|---|---|
| `bear-trail-icon.png` | アプリアイコン | 512 × 512px（正方形） |
| `bear-trail-1.png`〜`bear-trail-4.png` | スクリーンショット | 縦向き（例 1170 × 2532px） |
| `national-flag-quest-icon.png` | アプリアイコン（あおくんの国旗クエスト） | 512 × 512px（正方形） |
| `national-flag-quest-1.png`〜`national-flag-quest-4.png` | スクリーンショット（あおくんの国旗クエスト） | 縦向き（例 1170 × 2532px） |
| `block-puzzle-icon.png` | アプリアイコン（あおくんのブロックパズル・配置済み 512×512） | 512 × 512px（正方形） |
| `block-puzzle-1.png`〜`block-puzzle-4.png` | スクリーンショット（あおくんのブロックパズル・未配置） | 縦向き（例 1170 × 2532px） |
| `word-puzzle-icon.png` | アプリアイコン（あおくんの英単語パズル・配置済み 512×512） | 512 × 512px（正方形） |
| `word-puzzle-1.png`〜`word-puzzle-4.png` | スクリーンショット（あおくんの英単語パズル・未配置） | 縦向き（例 1170 × 2532px） |
| `license-museum-icon.png` | アプリアイコン（あおくんの資格博物館・配置済み 512×512） | 512 × 512px（正方形） |
| `license-museum-1.png`〜`license-museum-4.png` | スクリーンショット（あおくんの資格博物館・未配置） | 縦向き（例 1170 × 2532px） |

> `block-puzzle-icon.png` / `-thumb.png` は `tools/make_app_images.py` でアプリアイコンから生成しています（他アプリも同スクリプトで統一可能）。

他のアプリの詳細ページを作るときも、同じ命名ルール（`アプリ名-icon.png` / `アプリ名-1.png`…）で用意すると分かりやすいです。

---

### 画像がまだ無い場合
画像を入れなくてもサイト自体は正しく表示されます（グレーの枠にファイル名が表示されるだけ）。
画像が用意でき次第、このフォルダに置いてください。
