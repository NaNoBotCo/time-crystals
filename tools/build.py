"""Wrap page.html (the artifact body) into docs/index.html with the head GitHub Pages needs."""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
page = (root / "page.html").read_text()
title = re.search(r"<title>(.*?)</title>", page).group(1)
page = page.replace(f"<title>{title}</title>\n", "", 1)
url = "https://nanobotco.github.io/time-crystals/"
desc = "Time crystals as toys: salt next to a time crystal, a boot that kicks magnets, a sloppy kick that a crowd of magnets shrugs off, a jar that won't heat up, two foam beads lifted by sound, a levitator you can build, and a sentence you finish yourself. English and Thai."
head = f"""<!doctype html>
<html lang="en" translate="no" class="notranslate">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="google" content="notranslate">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="NaNoBotCo">
<meta property="og:title" content="Time Crystals, Drawn · ผลึกเวลา วาดให้ดู">
<meta property="og:description" content="Kick 'em every beat, they come home every other kick. · เตะทุกจังหวะ มันกลับบ้านทุกสองเตะ">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{url}card.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="A fence at night with magnets on the posts, flipping up and down, and the words Time Crystals, Drawn in English and Thai.">
<meta property="og:locale" content="en_US"><meta property="og:locale:alternate" content="th_TH">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{url}card.jpg">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}[hidden]{{display:none!important}}</style>
"""
i = page.index("<!--body-->")
out = head + page[:i] + "</head>\n<body>\n" + page[i + len("<!--body-->"):] + "\n</body>\n</html>\n"
(root / "docs" / "index.html").write_text(out)
print(root / "docs" / "index.html")

# sitemap, so the portal's robots.txt and the fleet roster can name it
import datetime
today = datetime.date.today().isoformat()
(root / "docs" / "sitemap.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{url}</loc><lastmod>{today}</lastmod></url>
</urlset>
""")
(root / "docs" / "llms.txt").write_text("""# Time Crystals, Drawn · ผลึกเวลา วาดให้ดู

Time crystals explained with toys you drive, in English and Thai, for readers of any language.

- Film: What's a time crystal? NaN and Beer, 15 minutes in 13 chapters, words on screen: https://nanobotco.github.io/time-crystals/film/what-is-a-time-crystal.mp4 (Thai: film/what-is-a-time-crystal-th.mp4). Chapters: can we time travel now?; what's a crystal; what's a time crystal; kick it; the sloppy boot; won't it get hot; no boot at all; what it ain't (time machine, free power, a clock, a rock in your hand); who made 'em; one you can build; the Chronos kit; what it's good for; say it back.
- Plain ol' crystal: guess the next ball in a salt checkerboard, then the next magnet across time. A pattern is something you can guess.
- Kick it: kick a fence of magnets at your own tempo; they come home every second kick, at half your beat. Stop kicking and they stop.
- The sloppy boot: kicks that turn the magnets only most of the way. Alone they drift off the beat; with neighbours joined they pull a knocked magnet back. Cartoon of the math.
- Won't it get hot?: set a magnet on fire; in a plain jar the heat spreads, in mud (disorder) it stays put.
- No boot at all: Hamburg 2022, a steady light on atoms between mirrors pulses on its own above a brightness threshold; a nudge moves the start, not the pace.
- One you can build: New York 2026 (Morrell, Elliott & Grier, Phys. Rev. Lett. 136, 057201): two foam beads in a 40 kHz levitator swing opposite ways at about 67 Hz when their sizes differ a little.
- Build one: Chronos, plans and code at https://github.com/NaNoBotCo/chronos; a parts kit on a sliding scale ($129 / $149 / $199).
- What it ain't: not a time machine, not free power (Watanabe & Oshikawa 2015), not just a clock.
- Who made 'em: Wilczek 2012 to Aalto 2025 and NYU 2026.

Cites: Wilczek PRL 109 (2012); Watanabe & Oshikawa PRL 114 (2015); Khemani et al. PRL 116 (2016); Else, Bauer & Nayak PRL 117 (2016); Zhang et al. and Choi et al. Nature 543 (2017); Randall et al. Science 374 (2021); Mi et al. Nature 601 (2022); Kongkhambut et al. Science 377 (2022); Zhao & Smalyukh Nature Materials (2025); Mäkinen et al. Nature Communications (2025); Morrell, Elliott & Grier PRL 136 (2026); Marzo, Barnes & Drinkwater RSI 88 (2017). Text CC BY 4.0, code MIT.
""")
