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
