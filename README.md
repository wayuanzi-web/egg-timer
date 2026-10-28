# 煮蛋計時器

單頁網頁 App：選一種蛋（沸水下蛋、冷水起煮、溫泉蛋），按開始就倒數，階段切換時叮一聲、震動、用中文語音講下一步，時間到連續響鈴，之後可以接著倒數泡冰水。也能自訂任何倒數（名稱、時間、第幾分鐘提醒什麼）。

純 HTML、CSS、JavaScript，沒有框架、不連任何外部網址。設定與自訂倒數只存在使用者裝置的瀏覽器裡（`localStorage`，鍵值前綴 `eggtimer:`），不上傳。

## 使用

- 網址：https://wayuanzi-web.github.io/egg-timer/
- 傳給別人時在網址後面加 `?openExternalBrowser=1`，LINE 會直接用手機瀏覽器開（頁面最下面「分享連結」就是這個）。
- iPhone：Safari 開網址 → 分享 → 加入主畫面。Android：Chrome 開網址 → 頁面最下面「安裝到這台裝置」。
- 煮的時候讓畫面開著；App 會申請螢幕常亮。切到別的 App 時提醒可能延後。

## 檔案

```
index.html              全部的畫面、資料與邏輯（資料在 <script> 最上面的 GROUPS）
manifest.webmanifest    PWA 設定
sw.js                   離線快取；只動 eggtimer- 前綴的快取
icon-192.png / icon-512.png / icon-maskable-512.png / apple-touch-icon.png
tools/make-icons.py     重新產生圖示（需要 Pillow）
```

## 修改與上線

1. 改 `index.html`。要加一種蛋或別的食物，在 `GROUPS` 裡照現有格式加一筆：`phases` 是一段段的倒數（`wait:true` 表示「等水滾」這種要人按下一步的階段），`finish` 是時間到的提示，`ice` 是之後泡冰水的秒數。
2. 改版時把 `sw.js` 的 `VERSION` 和 `index.html` 最下面的 `VERSION` 一起改。
3. `git add -A && git commit -m "..." && git push`，推上去約一分鐘後生效。手機第一次開還是舊版並在背景更新，第二次開就是新版，資料不受影響。

GitHub Pages 從 `main` 分支根目錄發布。
