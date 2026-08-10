/* =========================================================================
   アクセス解析（GoatCounter）
   -------------------------------------------------------------------------
   訪問者数・流入元などをバックエンドで集計する（訪問者の画面には何も表示しない）。
   Cookie を使わずプライバシーに配慮した方式のため、同意バナーは不要。

   ▼ 有効化の手順（一度だけ）
     1. https://www.goatcounter.com で無料アカウントを作成
        （例: コード名を "iruk" にすると https://iruk.goatcounter.com が管理画面）
     2. 発行された「あなたのサイトのcount URL」を下の GOATCOUNTER_ENDPOINT に設定
        例: "https://iruk.goatcounter.com/count"
     3. コミットして反映（全ページ共通で計測が有効になる）
   空文字のままなら計測タグは読み込まれず、無駄な通信も発生しない。
   ========================================================================= */
var GOATCOUNTER_ENDPOINT = ""; /* 例: "https://iruk.goatcounter.com/count" */

(function () {
  if (!GOATCOUNTER_ENDPOINT) return; /* 未設定なら何もしない */
  window.goatcounter = window.goatcounter || {};
  window.goatcounter.endpoint = GOATCOUNTER_ENDPOINT;
  var s = document.createElement("script");
  s.async = true;
  s.src = "//gc.zgo.at/count.js";
  s.setAttribute("data-goatcounter", GOATCOUNTER_ENDPOINT);
  (document.body || document.head || document.documentElement).appendChild(s);
})();

/* Mobile nav toggle */
document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
    });
  }

  /* Category filter (apps page) */
  var filterBtns = document.querySelectorAll(".filter-btn");
  var cards = document.querySelectorAll(".app-card[data-category]");
  if (filterBtns.length) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var cat = btn.getAttribute("data-filter");
        filterBtns.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        cards.forEach(function (card) {
          var match = cat === "all" || card.getAttribute("data-category") === cat;
          card.classList.toggle("hide", !match);
        });
      });
    });
  }
});
