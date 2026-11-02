# Exodia '26 — email footer

Signature footer modelled on the reference design: italic *Thanks & Regards*, the Exodia
logo tile, a thin divider, then name / phone / website / email, with IEDC Bootcamp,
FOCES and μLearn in an "Organised by" row.

All logos come from the official **Exodia 4.0** brand set
(`exodia-4-0.vercel.app/brand/` — repo `sarin-ms/exodia-4.0`).

## Using it

| Step | |
| --- | --- |
| 1 | Open `paste-into-gmail.html` in a browser |
| 2 | Ctrl+A, Ctrl+C |
| 3 | Gmail → Settings → Signature → paste → Save |

`test-email.eml` is a ready-made self-addressed test (To/From `exodiacec@gmail.com`);
open it in your mail client and press Send to see the footer arriving in an inbox.

## Live assets

```
https://sebin-gg.github.io/exodia26-footer/assets/
```

Repo: <https://github.com/sebin-gg/exodia26-footer> (public — free Pages requires it).

## Files

| File | What it is |
| --- | --- |
| `paste-into-gmail.html` | **Copy from this.** Live image URLs, so Gmail keeps the images. |
| `footer.html` | Dark footer source (for a mailer or HTML editor). |
| `footer-light.html` | Light twin, same content, ink logos. |
| `test-email.eml` | Self-addressed test message with the footer as its HTML body. |
| `preview.png`, `preview-light.png` | Rendered look-checks (base64 inlined — never paste these). |
| `assets/` | Generated logos plus the `ref-*` SVG sources and `_raw-*` renders. |
| `make_assets.py` | Regenerates every image: `python make_assets.py`. |
| `ref/` | The WhatsApp reference video. |

## Details

- **Title** — EXODIA '26 / All Kerala Tech Gala
- **Phone** — `+91 70126 84869` → `tel:+917012684869`
- **Website** — `https://www.exodiacec.in`
- **Email** — `exodiacec@gmail.com`
- **Links** — FOCES → `foces.ceconline.edu`, μLearn → `mulearn.org`, tile → `exodiacec.in`

## Why the logos are PNG/GIF

Mail clients will not render SVG, so each brand SVG is rasterised with headless Chrome
into `assets/_raw-*.png`, then `make_assets.py` cuts the tiles and recolours for light.

The four marks are **single-colour cream** artwork drawn for a dark background, which is
why there are no white logo pills any more: the dark footer uses the cream originals, and
the light footer gets ink recolours of the same shapes.

## Weight

| | dark | light |
| --- | --- | --- |
| images | 23.6 KB | 19.4 KB |
| markup (no comments) | 6.3 KB | 6.3 KB |
| **total** | **30.0 KB** | **25.7 KB** |

The tile is a 208 px, 16-colour, 8-frame GIF (`exodia-tile.gif` 15.3 KB). Frame 0 is the
finished logo, so a client that never animates it — or any thumbnail — still shows the
complete mark.

## Surviving a hostile paste

- Dark fill lives on the `<td>` as **both** `bgcolor` and inline `background-color`, and is
  repeated on the wrapping table: Gmail's signature editor and Outlook drop table styles
  more readily than a cell background.
- Every text run is wrapped in `<font color>`, so if inline CSS is stripped entirely the
  text still contrasts with the card.
- Real alt text on every image; phone, site and email are live text links.
- Linear nested tables keep the reading order when `<style>` is removed; that block only
  adds mobile stacking below 480 px.
