(function () {
  var header = document.querySelector("[data-header]");
  if (!header) return;

  function updateHeader() {
    if (window.scrollY > 18) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  }

  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });
})();
