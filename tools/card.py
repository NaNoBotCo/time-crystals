"""Share card, 1200x630: a fence at night, magnets on the posts taking turns up and down, and the title."""
import math, pathlib
from PIL import Image, ImageDraw, ImageFont

out = pathlib.Path(__file__).resolve().parent.parent / "docs" / "card.jpg"
W, H = 1200, 630
S = 2
img = Image.new("RGB", (W * S, H * S))
d = ImageDraw.Draw(img)
top, bot = (4, 6, 15), (23, 33, 63)
for y in range(H * S):
    u = min(1, y / (H * S * .8))
    d.line([(0, y), (W * S, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * u) for i in range(3)))
STAR, GLOW, GOLD, INK, PANEL, WELL, WOOD = (255, 244, 210), (255, 226, 122), (241, 193, 61), (233, 237, 247), (19, 26, 45), (27, 36, 64), (178, 124, 77)
import random
r = random.Random(5)
for _ in range(160):
    x, y, s = r.random() * W, r.random() * H * .55, r.random() * 1.6 + .5
    d.ellipse([(x - s) * S, (y - s) * S, (x + s) * S, (y + s) * S], fill=STAR)

def hill(x, k):
    return H * (.66 + .1 * k) + math.sin(x / (230 + 60 * k) + k * 2) * 26 + math.sin(x / 97 + k) * 9

for col, k in [((21, 32, 57), 0), ((16, 24, 47), 1)]:
    d.polygon([(0, H * S)] + [(x * S, hill(x, k) * S) for x in range(0, W + 20, 10)] + [(W * S, H * S)], fill=col)
for i, x in enumerate(range(800, W, 70)):
    y = hill(x, 2) - 6
    d.rectangle([(x - 6) * S, (y - 60) * S, (x + 6) * S, (y + 6) * S], fill=WOOD)
    mx, my, rr = x, y - 88, 22
    d.ellipse([(mx - rr) * S, (my - rr) * S, (mx + rr) * S, (my + rr) * S], fill=PANEL, outline=INK, width=3 * S)
    sgn = -1 if i % 2 == 0 else 1
    tip = [(mx * S, (my + sgn * rr * .8) * S), ((mx + rr * .32) * S, my * S), ((mx - rr * .32) * S, my * S)]
    tail = [(mx * S, (my - sgn * rr * .8) * S), ((mx + rr * .32) * S, my * S), ((mx - rr * .32) * S, my * S)]
    d.polygon(tail, fill=WELL, outline=INK)
    d.polygon(tip, fill=GOLD, outline=INK)
for x in range(770, W, 6):
    y = hill(x, 2) - 50
    d.rectangle([x * S, y * S, (x + 6) * S, (y + 7) * S], fill=WOOD)
    d.rectangle([x * S, (y + 28) * S, (x + 6) * S, (y + 34) * S], fill=WOOD)
d.polygon([(0, H * S)] + [(x * S, hill(x, 2) * S) for x in range(0, W + 20, 10)] + [(W * S, H * S)], fill=(11, 17, 35))
for _ in range(12):
    x, y = 790 + r.random() * 390, H * (.5 + r.random() * .38)
    d.ellipse([(x - 8) * S, (y - 8) * S, (x + 8) * S, (y + 8) * S], fill=(40, 44, 52))
    d.ellipse([(x - 3) * S, (y - 3) * S, (x + 3) * S, (y + 3) * S], fill=GLOW)
img = img.resize((W, H), Image.LANCZOS)
d = ImageDraw.Draw(img)
F = "/System/Library/Fonts/Supplemental/"
big = ImageFont.truetype(F + "Georgia Bold.ttf", 92)
th = ImageFont.truetype(F + "Tahoma Bold.ttf", 54)
small = ImageFont.truetype(F + "Courier New Bold.ttf", 28)
thsmall = ImageFont.truetype(F + "Tahoma.ttf", 30)
d.text((64, 96), "A 'SPLAINER, WITH TOYS", font=small, fill=GOLD)
d.text((60, 140), "Time Crystals,", font=big, fill=INK)
d.text((60, 240), "Drawn", font=big, fill=INK)
d.text((64, 352), "ผลึกเวลา วาดให้ดู", font=th, fill=(163, 172, 196))
d.text((64, 446), "Kick every beat. Home every other kick.", font=small, fill=INK)
d.text((64, 488), "เตะทุกจังหวะ กลับบ้านทุกสองเตะ", font=thsmall, fill=(163, 172, 196))
d.text((64, 566), "nanobotco.github.io/time-crystals", font=small, fill=GOLD)
img.save(out, quality=88)
print(out)
