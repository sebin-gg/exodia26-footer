"""Build the image assets for the Exodia '26 email footer.

Every logo comes from the official brand set published with Exodia 4.0
(exodia-4-0.vercel.app/brand/): exodia-mark.svg, foces.svg, iedc-bootcamp.svg
and mulearn.svg. Mail clients will not render SVG, so each one is rasterised
to a PNG here (see README for the headless-Chrome step that produces the
assets/_raw-*.png sources).

Those marks are single-colour cream artwork drawn for a dark background, which
drives the whole approach:
  - dark footer  -> the cream originals, used as-is;
  - light footer -> the same shapes recoloured to ink.
No white logo pills are needed any more, which also saves bytes.

Outputs (all in ./assets):
  exodia-tile.gif / .png              - animated tile, cream mark on dark
  exodia-tile-light.gif / .png        - animated tile, ink mark on white
  foces-cream.png     foces-ink.png
  iedc-cream.png      iedc-ink.png
  mulearn-cream.png   mulearn-ink.png

Animation has to be a GIF: Gmail and Outlook strip SVG, CSS animations and
<canvas>, so a GIF is the only thing that actually moves inside an inbox.
Frame 0 is the finished logo, so a client that never animates it still shows
a complete mark.
"""

import math
import os
from collections import Counter

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

W = H = 208                      # 2x the 104px display size
PAD = 30                         # breathing room inside the tile
COLOURS = 16                     # palette size; these marks are near-flat
TILE_DARK = (23, 20, 34)          # --color-cinder from exodia-4-0.vercel.app
TILE_LIGHT = (255, 255, 255)
INK = (15, 17, 19)
# per-brand colours for the light footer: muLearn blue, FOCES ink, IEDC cyan
BRAND = {"mulearn": (65, 121, 251), "foces": INK, "iedc-bootcamp": (31, 163, 221)}

RAW = {
    "exodia-mark": "_raw-exodia-mark.png",
    "foces": "_raw-foces.png",
    "iedc-bootcamp": "_raw-iedc-bootcamp.png",
    "mulearn": "_raw-mulearn.png",
}

# every "Organised by" logo is centred on an identical transparent canvas, so
# all three occupy exactly the same space in every mail client, whatever their
# native aspect ratio and whatever CSS the client supports
ROW = ["foces", "iedc-bootcamp", "mulearn"]
BOX_W, BOX_H = 176, 56           # 2x of the 88x28 display box

STALE = [
    "iedc-animated.gif", "iedc-static.png", "foces-dark.png",
    "mulearn.png", "exodia-mark.png",
]


def load_raw(name):
    im = Image.open(os.path.join(ASSETS, RAW[name])).convert("RGBA")
    bbox = im.getchannel("A").getbbox()
    return im.crop(bbox) if bbox else im


def brand_cream(name="exodia-mark"):
    """Sample the single ink colour the brand marks are drawn in."""
    im = load_raw(name)
    opaque = [px for px in im.getdata() if px[3] > 200] or [(235, 221, 203, 255)]
    r, g, b, _ = Counter((p[0], p[1], p[2], 255) for p in opaque).most_common(1)[0][0]
    return (r, g, b)


def recolour(mark, colour):
    out = Image.new("RGBA", mark.size, tuple(colour) + (0,))
    out.putalpha(mark.getchannel("A"))
    return out


def fit(mark, box, scale=1.0):
    ratio = min(box / mark.width, box / mark.height) * scale
    return mark.resize(
        (max(1, int(mark.width * ratio)), max(1, int(mark.height * ratio))), Image.LANCZOS
    )


def tile(mark, bg, scale=1.0, alpha=1.0):
    """Composite the mark centred on a flat tile at the given scale/alpha."""
    img = Image.new("RGB", (W, H), bg)
    m = fit(mark, W - 2 * PAD, scale)
    if alpha < 1.0:
        m = m.copy()
        m.putalpha(m.getchannel("A").point(lambda v: int(v * alpha)))
    img.paste(m, ((W - m.width) // 2, (H - m.height) // 2), m)
    return img


def build_tile(mark, bg, gif_name, png_name):
    final = tile(mark, bg)
    seq = []                                   # [(image, duration_ms)]

    def add(img, ms):
        if seq and img.tobytes() == seq[-1][0].tobytes():
            seq[-1] = (seq[-1][0], seq[-1][1] + ms)
        else:
            seq.append((img, ms))

    # Frame 0 is the finished logo: a client that never animates the GIF,
    # or any thumbnail, still shows a complete mark.
    add(final, 1800)

    # smooth cosine breath, ending exactly on the frame it started from
    steps = 6
    for i in range(1, steps + 1):
        phase = (1 - math.cos(2 * math.pi * i / (steps + 1))) / 2
        add(tile(mark, bg, scale=1.0 + 0.06 * phase), 240)

    # short pause between cycles so the breath is not continuous
    add(final, 1100)

    frames = [f for f, _ in seq]
    durations = [d for _, d in seq]

    master = frames[len(frames) // 2].quantize(colors=COLOURS, method=Image.MEDIANCUT, dither=Image.NONE)
    pal = [f.quantize(palette=master, dither=Image.NONE) for f in frames]

    pal[0].save(
        os.path.join(ASSETS, gif_name),
        save_all=True,
        append_images=pal[1:],
        duration=durations,
        loop=0,
        optimize=False,
        disposal=2,
    )
    final.save(os.path.join(ASSETS, png_name))
    return len(frames)


WORDMARK_HEIGHT = 52


def build_wordmark(cream):
    """Small Exodia mark used beside the title, at 2x its 26px display size."""
    mark = load_raw("exodia-mark")
    sized = mark.resize(
        (max(1, round(mark.width * WORDMARK_HEIGHT / mark.height)), WORDMARK_HEIGHT),
        Image.LANCZOS,
    )
    recolour(sized, cream).save(os.path.join(ASSETS, "exodia-mark-cream.png"), optimize=True)
    recolour(sized, INK).save(os.path.join(ASSETS, "exodia-mark-ink.png"), optimize=True)


def fit_box(mark, width, height):
    ratio = min(width / mark.width, height / mark.height)
    return mark.resize(
        (max(1, int(mark.width * ratio)), max(1, int(mark.height * ratio))), Image.LANCZOS
    )


def build_row_logos(cream):
    for name in ROW:
        mark = fit_box(load_raw(name), BOX_W, BOX_H)
        for suffix, colour in (("cream", cream), ("ink", BRAND.get(name, INK))):
            canvas = Image.new("RGBA", (BOX_W, BOX_H), (0, 0, 0, 0))
            coloured = recolour(mark, colour)
            canvas.alpha_composite(
                coloured,
                ((BOX_W - coloured.width) // 2, (BOX_H - coloured.height) // 2),
            )
            flat = canvas.convert("RGB").quantize(colors=32, method=Image.FASTOCTREE).convert("RGB")
            packed = flat.convert("RGBA")
            packed.putalpha(canvas.getchannel("A"))
            packed.save(os.path.join(ASSETS, "%s-%s.png" % (name, suffix)), optimize=True)


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    cream = brand_cream()
    print("brand cream:", cream)

    exo = load_raw("exodia-mark")
    print("dark tile frames:", build_tile(exo, TILE_DARK, "exodia-tile.gif", "exodia-tile.png"))
    print("light tile frames:", build_tile(recolour(exo, INK), TILE_LIGHT,
                                          "exodia-tile-light.gif", "exodia-tile-light.png"))

    build_row_logos(cream)
    build_wordmark(cream)

    for name in STALE:
        path = os.path.join(ASSETS, name)
        if os.path.exists(path):
            os.remove(path)
            print("removed stale", name)

    groups = {
        "dark footer": ["exodia-tile.gif", "foces-cream.png", "iedc-bootcamp-cream.png", "mulearn-cream.png", "exodia-mark-cream.png"],
        "light footer": ["exodia-tile-light.gif", "foces-ink.png", "iedc-bootcamp-ink.png", "mulearn-ink.png", "exodia-mark-ink.png"],
    }
    for label, names in groups.items():
        total = 0
        for n in names:
            path = os.path.join(ASSETS, n)
            if os.path.exists(path):
                size = os.path.getsize(path)
                total += size
                print("  %-28s %5.1f KB" % (n, size / 1024))
        print("%s images: %.1f KB" % (label, total / 1024))
