# Iruk Homepage

Irukの個人ホームページ（アプリ開発ポートフォリオ）。静的HTML/CSS/JSのみで動きます。

## 構成
```
iruk-homepage/
├── index.html            ホーム（自己紹介・注目アプリ・SNS）
├── apps.html             アプリ一覧（カテゴリ絞り込み付き）
├── contact.html          お問い合わせフォーム
├── apps/
│   ├── bear-trail.html            アプリ紹介ページ（実例）
│   └── bear-trail-privacy.html    プライバシーポリシー（実例）
├── css/style.css         デザイン（ライト/ダーク対応）
├── js/main.js            メニュー開閉・カテゴリ絞り込み
└── images/               画像置き場（images/README.md に必要な画像一覧）
```

## ページの関係
- `apps.html` → 各アプリ紹介ページ（`apps/*.html`）→ 各プライバシーポリシー（`apps/*-privacy.html`）
- 新しいアプリを追加するときは `apps/bear-trail.html` と `apps/bear-trail-privacy.html` を
  コピーして中身を差し替え、`apps.html` にカードを1枚追加すればOKです。

## カテゴリ
あおくんシリーズ / ボードゲーム / ライフスタイル / その他
（カテゴリを増やす場合：`apps.html` のフィルターボタンとカードの `data-category`、`css` の `.badge` 色を追加）

## お問い合わせフォームの設定（重要）
`contact.html` のフォームは [Formspree](https://formspree.io)（無料枠あり）を使う想定です。
1. Formspreeに登録してフォームを作成
2. 発行されたIDを `contact.html` の `action="https://formspree.io/f/your-id"` と差し替え

設定するまで送信は動作しません。

## 表示確認
`index.html` をブラウザで開くだけで確認できます。

## 公開方法（例）
- **GitHub Pages**：このリポジトリをGitHubにpushし、Settings → Pages で公開
- **Netlify / Cloudflare Pages**：フォルダをドラッグ＆ドロップ、または連携でデプロイ
