#!/usr/bin/env python3
"""apps.html のアプリカードから、カテゴリ別ページ categories.html を生成する。

apps.html の各 <a class="app-card" data-category="..."> をカテゴリごとに集め、
カテゴリ見出し（絵文字＋名前＋説明＋件数）付きのセクションに並べた独立ページを出力する。
アプリを追加・編集したら apps.html を直してから本スクリプトを再実行すれば categories.html も揃う。

使い方:
  python tools/build_categories.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 表示順とカテゴリのメタ情報（data-category の値 → 見出し）
CATEGORIES = [
    ("aokun", "🐱", "あおくんシリーズ",
     "ロシアンブルーの子猫「あおくん」がナビ役。遊びながら学べる、教育＆カジュアルアプリのシリーズです。"),
    ("board", "🎮", "インディーズゲーム",
     "じっくり遊べるオリジナルゲーム。ボードゲームや推理ゲームなど、こだわって作った自作ゲーム作品です。"),
    ("life", "🌱", "ライフスタイル",
     "毎日の暮らしを、ちょっと便利に・心地よく。日常に寄り添うツール系アプリです。"),
]

HEAD = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>カテゴリ | Iruk</title>
  <meta name="description" content="Irukのアプリをカテゴリ別に紹介。あおくんシリーズ、インディーズゲーム、ライフスタイルの3カテゴリで開発中・配信中のアプリをまとめています。" />
  <link rel="icon" type="image/png" href="images/favicon.png" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <header class="site-header">
    <div class="container nav">
      <a href="index.html" class="brand">Iruk<span>.</span></a>
      <button class="nav-toggle" aria-label="メニュー">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
      <ul class="nav-links">
        <li><a href="index.html">ホーム</a></li>
        <li><a href="apps.html">アプリ一覧</a></li>
        <li><a href="categories.html">カテゴリ</a></li>
        <li><a href="contact.html">お問い合わせ</a></li>
        <li><a href="https://x.com/pieefo" target="_blank" rel="noopener">X</a></li>
      </ul>
    </div>
  </header>

  <div class="container">
    <nav class="breadcrumb"><a href="index.html">ホーム</a> ／ カテゴリ</nav>
  </div>

  <section class="section" style="padding-bottom:8px;">
    <div class="container">
      <h1 class="section-title">カテゴリ</h1>
      <p class="section-lead">ジャンルごとにアプリをまとめました</p>
    </div>
  </section>
"""

FOOTER = """
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <h4>Iruk</h4>
          <p style="color:var(--text-muted); font-size:.9rem; max-width:260px;">個人アプリ開発者。さまざまなジャンルのアプリを制作中。</p>
          <div class="social">
            <a href="https://x.com/pieefo" target="_blank" rel="noopener" aria-label="X (Twitter)">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 2H22l-7.6 8.7L23 22h-6.9l-5.4-7-6.2 7H1.3l8.1-9.3L1 2h7.1l4.9 6.5L18.9 2Zm-2.4 18h1.9L7.6 4H5.6l10.9 16Z"/></svg>
            </a>
          </div>
        </div>
        <div>
          <h4>メニュー</h4>
          <ul class="footer-links">
            <li><a href="index.html">ホーム</a></li>
            <li><a href="apps.html">アプリ一覧</a></li>
            <li><a href="categories.html">カテゴリ</a></li>
            <li><a href="contact.html">お問い合わせ</a></li>
          </ul>
        </div>
        <div>
          <h4>カテゴリ</h4>
          <ul class="footer-links">
            <li><a href="categories.html">あおくんシリーズ</a></li>
            <li><a href="categories.html">インディーズゲーム</a></li>
            <li><a href="categories.html">ライフスタイル</a></li>
          </ul>
        </div>
      </div>
      <p class="copyright">© 2026 Iruk. All rights reserved.</p>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""


def extract_cards(html: str):
    """apps.html から data-category ごとに app-card ブロックを集める。"""
    cards = {}
    for m in re.finditer(
            r'<a\b[^>]*class="app-card"[^>]*data-category="([^"]+)"[^>]*>.*?</a>',
            html, re.S):
        cat = m.group(1)
        cards.setdefault(cat, []).append(m.group(0).strip())
    return cards


def main():
    apps_html = (ROOT / "apps.html").read_text(encoding="utf-8")
    cards = extract_cards(apps_html)

    parts = [HEAD]
    for i, (key, emoji, name, desc) in enumerate(CATEGORIES):
        group = cards.get(key, [])
        if not group:
            continue
        bg = ' style="background:var(--surface);"' if i % 2 == 1 else ""
        cards_html = "\n\n".join("        " + c.replace("\n", "\n") for c in group)
        parts.append(f"""
  <section class="section cat-section" id="{key}"{bg}>
    <div class="container">
      <div class="cat-head">
        <span class="cat-emoji">{emoji}</span>
        <div>
          <h2>{name} <span class="cat-count">{len(group)}アプリ</span></h2>
          <p>{desc}</p>
        </div>
      </div>
      <div class="card-grid">
{cards_html}
      </div>
    </div>
  </section>
""")
    parts.append(FOOTER)
    out = ROOT / "categories.html"
    out.write_text("".join(parts), encoding="utf-8", newline="")
    total = sum(len(cards.get(k, [])) for k, *_ in CATEGORIES)
    print(f"wrote {out.name}  カテゴリ{len([1 for k,*_ in CATEGORIES if cards.get(k)])} / アプリ{total}件")
    for key, _, name, _ in CATEGORIES:
        print(f"  {name}: {len(cards.get(key, []))}件")


if __name__ == "__main__":
    main()
