#!/usr/bin/env python3
"""產生 App 圖示：深色底、蛋白、蛋黃。
用法：python3 tools/make-icons.py（在 repo 根目錄執行，需要 Pillow）"""
from PIL import Image, ImageDraw
import os

BG = (16, 24, 26)        # 與 App 深色背景相同
SHELL = (255, 253, 246)  # 蛋白
EDGE = (205, 191, 166)   # 蛋殼邊
YOLK = (226, 144, 12)    # 蛋黃（App 主色）
GLOSS = (255, 236, 196)

def draw(size, pad_ratio, radius_ratio, out):
    s = size * 4  # 先畫大再縮小，邊緣才平滑
    im = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    r = int(s * radius_ratio)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=r, fill=BG)
    pad = int(s * pad_ratio)
    # 蛋：橢圓，稍微上窄下寬
    ex0, ey0, ex1, ey1 = pad, pad - int(s * 0.02), s - pad, s - pad + int(s * 0.02)
    d.ellipse([ex0, ey0, ex1, ey1], fill=SHELL, outline=EDGE, width=int(s * 0.018))
    cx, cy = s // 2, int(s * 0.54)
    yr = int((ex1 - ex0) * 0.27)
    d.ellipse([cx - yr, cy - yr, cx + yr, cy + yr], fill=YOLK)
    gr = int(yr * 0.32)
    d.ellipse([cx - yr * 0.45 - gr, cy - yr * 0.45 - gr * 0.6, cx - yr * 0.45 + gr, cy - yr * 0.45 + gr * 0.6], fill=GLOSS)
    im = im.resize((size, size), Image.LANCZOS)
    im.save(out)
    print(out, size)

os.makedirs('.', exist_ok=True)
draw(192, 0.16, 0.2, 'icon-192.png')
draw(512, 0.16, 0.2, 'icon-512.png')
draw(512, 0.24, 0.0, 'icon-maskable-512.png')   # 可裁切：留 20% 以上安全區，底色填滿
draw(180, 0.16, 0.0, 'apple-touch-icon.png')     # iOS 自己加圓角
