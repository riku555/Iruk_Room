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
