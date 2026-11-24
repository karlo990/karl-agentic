// Studio: download all five slides of a post at once (zip), save them to a phone, copy captions.
(function () {
  var grid = document.getElementById('studio-grid');
  if (!grid) return;
  var posts = [], toast = document.getElementById('toast'), tt;
  function say(m) { toast.textContent = m; toast.classList.add('on'); clearTimeout(tt); tt = setTimeout(function () { toast.classList.remove('on'); }, 2200); }
  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  var canShareFiles = !!(navigator.canShare && window.File && navigator.canShare({ files: [new File([''], 'a.jpg', { type: 'image/jpeg' })] }));

  function fetchBlobs(p) {
    return Promise.all(p.images.map(function (u) { return fetch(u).then(function (r) { if (!r.ok) throw new Error(u); return r.blob(); }); }));
  }
  function saveBlob(blob, name) {
    var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 4000);
  }
  function zipPosts(list, name, btn) {
    var label = btn.textContent; btn.disabled = true; btn.textContent = 'Preparing…';
    var zip = new JSZip();
    var jobs = list.map(function (p) {
      var folder = list.length > 1 ? zip.folder(p.slug) : zip;
      folder.file('caption.txt', p.caption);
      return fetchBlobs(p).then(function (blobs) { blobs.forEach(function (b, i) { folder.file(p.slug + '-' + (i + 1) + '.jpg', b); }); });
    });
    return Promise.all(jobs).then(function () { return zip.generateAsync({ type: 'blob' }); })
      .then(function (blob) { saveBlob(blob, name); say('Downloaded ' + name); })
      .catch(function () { say('Download failed. Check your connection and try again.'); })
      .then(function () { btn.disabled = false; btn.textContent = label; });
  }
  function sharePost(p, btn) {
    btn.disabled = true;
    fetchBlobs(p).then(function (blobs) {
      var files = blobs.map(function (b, i) { return new File([b], p.slug + '-' + (i + 1) + '.jpg', { type: 'image/jpeg' }); });
      return navigator.share({ files: files, title: p.title });
    }).catch(function (e) { if (e && e.name !== 'AbortError') say('Sharing is not available here. Use Download instead.'); })
      .then(function () { btn.disabled = false; });
  }
  function copy(text) {
    var ok = function () { say('Caption copied'); };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(ok, fb); else fb();
    function fb() { var t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select(); try { document.execCommand('copy'); ok(); } catch (e) { say('Select the caption to copy it'); } t.remove(); }
  }
  function render(filter) {
    grid.innerHTML = posts.filter(function (p) { return !filter || filter === 'All' || (filter === 'NVIDIA' ? p.nvidia : p.cat === filter); }).map(function (p) {
      var i = posts.indexOf(p);
      return '<article class="sp" data-i="' + i + '">' +
        '<button class="sp-cover" type="button" aria-label="Preview ' + esc(p.title) + '"><img src="' + p.thumbs[0] + '" alt="' + esc(p.pre + ' ' + p.title) + ' cover" loading="lazy" width="360" height="450">' + (p.nvidia ? '<span class="sp-nv">NVIDIA</span>' : '') + '<span class="sp-n">5 slides</span></button>' +
        '<div class="sp-body"><span class="eyebrow">' + esc(p.cat) + '</span><h3>' + esc(p.title) + '</h3><p>Gift: ' + esc(p.gift) + '</p>' +
        '<div class="sp-strip" hidden>' + p.thumbs.map(function (t, k) { return '<a href="' + p.images[k] + '" target="_blank" rel="noopener"><img src="' + t + '" alt="Slide ' + (k + 1) + '" loading="lazy" width="360" height="450"></a>'; }).join('') + '</div>' +
        '<div class="sp-actions"><button class="btn btn-pink sm" data-act="zip" type="button">Download all 5</button>' +
        (canShareFiles ? '<button class="btn btn-light sm" data-act="share" type="button">Save to phone</button>' : '') +
        '<button class="btn btn-light sm" data-act="cap" type="button">Copy caption</button></div>' +
        '<details class="sp-cap"><summary>Show caption</summary><pre>' + esc(p.caption) + '</pre></details></div></article>';
    }).join('');
  }
  grid.addEventListener('click', function (e) {
    var card = e.target.closest('.sp'); if (!card) return;
    var p = posts[+card.dataset.i], act = e.target.closest('[data-act]');
    if (e.target.closest('.sp-cover')) { var s = card.querySelector('.sp-strip'); s.hidden = !s.hidden; return; }
    if (!act) return;
    if (act.dataset.act === 'zip') zipPosts([p], p.slug + '.zip', act);
    if (act.dataset.act === 'share') sharePost(p, act);
    if (act.dataset.act === 'cap') copy(p.caption);
  });
  document.getElementById('studio-filters').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    document.querySelectorAll('#studio-filters button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    render(b.textContent);
  });
  var all = document.getElementById('dl-all');
  fetch('/studio/posts.json').then(function (r) { return r.json(); }).then(function (data) {
    posts = data; render('All');
    document.getElementById('studio-count').textContent = data.length + ' posts · ' + data.length * 5 + ' images';
    all.addEventListener('click', function () { zipPosts(posts, 'karl-agentic-studio-all.zip', all); });
  });
})();
