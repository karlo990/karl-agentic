// Mobile menu and copy buttons for prompts.
(function () {
  var btn = document.querySelector('.menu-btn'), nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) { if (e.target.tagName === 'A') { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); } });
  }
  var toast = document.getElementById('toast'), t;
  function say(m) { if (!toast) return; toast.textContent = m; toast.classList.add('on'); clearTimeout(t); t = setTimeout(function () { toast.classList.remove('on'); }, 1800); }
  document.querySelectorAll('.copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var text = b.parentElement.querySelector('pre').innerText;
      var done = function () { b.textContent = 'Copied'; say('Prompt copied'); setTimeout(function () { b.textContent = 'Copy'; }, 1500); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () { fallback(text, done); });
      else fallback(text, done);
    });
  });
  function fallback(text, done) {
    var ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); done(); } catch (e) { say('Select the text to copy it'); }
    ta.remove();
  }
})();
