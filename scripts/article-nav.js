(function () {
  var art = document.querySelector(".fm-article");
  if (!art) return;
  var heads = Array.prototype.slice.call(art.querySelectorAll("h2[id]"));
  if (heads.length < 6) return;

  var nav = document.createElement("nav");
  nav.className = "fm-navsec";
  nav.setAttribute("aria-label", "Navegación por secciones");
  nav.innerHTML =
    '<button type="button" class="fm-navsec-btn" data-dir="-1" aria-label="Sección anterior"><span aria-hidden="true">&#8593;</span><span class="fm-navsec-txt">Anterior</span></button>' +
    '<button type="button" class="fm-navsec-cur" aria-haspopup="true" aria-expanded="false"><span class="fm-navsec-num"></span><span class="fm-navsec-name"></span></button>' +
    '<button type="button" class="fm-navsec-btn" data-dir="1" aria-label="Sección siguiente"><span class="fm-navsec-txt">Siguiente</span><span aria-hidden="true">&#8595;</span></button>';
  // Sin etiquetas de bloque en cadenas: wpautop las envuelve en <p> y rompe el script.
  var list = document.createElement("ul");
  list.className = "fm-navsec-list";
  list.hidden = true;
  nav.appendChild(list);
  heads.forEach(function (h, i) {
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = "#" + h.id;
    a.textContent = h.textContent;
    a.setAttribute("data-i", i);
    li.appendChild(a);
    list.appendChild(li);
  });
  document.body.appendChild(nav);
  art.classList.add("fm-has-navsec");

  var cur = -1, visible = false;
  var curBtn = nav.querySelector(".fm-navsec-cur");
  var numEl = nav.querySelector(".fm-navsec-num");
  var nameEl = nav.querySelector(".fm-navsec-name");
  var prevBtn = nav.querySelector('[data-dir="-1"]');
  var nextBtn = nav.querySelector('[data-dir="1"]');

  function shortTitle(t) {
    var i = t.indexOf(":");
    return (i > 6 && i < 40) ? t.slice(0, i) : t;
  }
  function render() {
    var i = Math.max(cur, 0);
    numEl.textContent = (cur + 1) + "/" + heads.length;
    nameEl.textContent = cur < 0 ? "Introducción" : shortTitle(heads[i].textContent);
    prevBtn.disabled = cur < 0;
    nextBtn.disabled = cur >= heads.length - 1;
    Array.prototype.forEach.call(list.querySelectorAll("a"), function (a, k) {
      if (k === cur) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
    });
  }
  function update() {
    var line = window.scrollY + Math.min(window.innerHeight * 0.3, 160);
    var c = -1;
    for (var i = 0; i < heads.length; i++) {
      if (heads[i].getBoundingClientRect().top + window.scrollY <= line) c = i; else break;
    }
    if (c !== cur) { cur = c; render(); }
    var top = art.getBoundingClientRect().top + window.scrollY;
    var bottom = top + art.offsetHeight;
    var show = window.scrollY > top + 300 && window.scrollY + window.innerHeight < bottom + 200;
    if (show !== visible) { visible = show; nav.classList.toggle("fm-navsec-on", show); if (!show) closeList(); }
  }
  function go(i) {
    closeList();
    if (i < 0) { window.scrollTo({ top: art.getBoundingClientRect().top + window.scrollY - 80, behavior: "smooth" }); return; }
    i = Math.min(i, heads.length - 1);
    heads[i].scrollIntoView({ behavior: "smooth", block: "start" });
    if (history.replaceState) history.replaceState(null, "", "#" + heads[i].id);
  }
  function closeList() { list.hidden = true; curBtn.setAttribute("aria-expanded", "false"); }
  function toggleList() {
    list.hidden = !list.hidden;
    curBtn.setAttribute("aria-expanded", String(!list.hidden));
    if (!list.hidden) {
      var a = list.querySelector('[aria-current="true"]');
      if (a) a.scrollIntoView({ block: "center" });
    }
  }

  prevBtn.addEventListener("click", function () { go(cur - 1); });
  nextBtn.addEventListener("click", function () { go(cur + 1); });
  curBtn.addEventListener("click", toggleList);
  list.addEventListener("click", function (e) {
    var a = e.target.closest("a");
    if (!a) return;
    e.preventDefault();
    go(parseInt(a.getAttribute("data-i"), 10));
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeList(); });
  document.addEventListener("click", function (e) { if (!nav.contains(e.target)) closeList(); });

  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () { update(); ticking = false; });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  update();
})();
