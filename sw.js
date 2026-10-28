/* 煮蛋計時器 service worker
   只快取、只清理自己（eggtimer- 前綴）的東西。wayuanzi-web.github.io 底下的網站共用同一個網域的儲存空間，
   所以絕對不碰別的網站的快取。換版時改 VERSION，舊快取會在下次啟用時刪掉。 */
const VERSION = '1.0.0';
const CACHE = 'eggtimer-' + VERSION;
const SCOPE = new URL(self.registration.scope).pathname;
const FILES = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png', './icon-maskable-512.png', './apple-touch-icon.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k.startsWith('eggtimer-') && k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin || !url.pathname.startsWith(SCOPE)) return;
  // 先回快取，同時在背景更新：第一次開是舊版，第二次開就是新版。
  e.respondWith(
    caches.open(CACHE).then(cache =>
      cache.match(req, { ignoreSearch: true }).then(cached => {
        const update = fetch(req).then(res => {
          if (res && res.ok) cache.put(req, res.clone());
          return res;
        }).catch(() => cached);
        return cached || update;
      })
    )
  );
});
