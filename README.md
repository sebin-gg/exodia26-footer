# Exodia '26 — email footer

Dark signature footer modelled on the reference design: italic *Thanks & Regards*,
white logo tile, thin divider, then name / phone / website / email. The tile is the
**IEDC mark animating** into place, and the FOCES + μLearn marks sit in a partner row.

## Files

| File | What it is |
| --- | --- |
| `footer.html` | The footer to paste into Gmail / your mailer. Image URLs use `ASSET_BASE`. |
| `preview.html` | Same footer with images inlined as base64 — open in a browser to check the look. Do **not** paste this one into email (Gmail strips data URIs). |
| `assets/` | Logos to upload: `iedc-animated.gif`, `iedc-static.png`, `foces-dark.png`, `mulearn.png`, plus sources (`foces.svg`, `exodia.svg`). |
| `make_assets.py` | Regenerates the animated IEDC tile and the logo files. Run `python make_assets.py`. |
| `ref/` | The WhatsApp reference video + frames. |

## Using it

1. Upload `assets/` somewhere with a public https URL (GitHub Pages, R2, S3, Netlify).
2. In `footer.html`, replace every `ASSET_BASE` with that URL, no trailing slash.
3. Paste the block into Gmail → Settings → Signature, or your mailer template.

## Details to check

- **Email** — `exodiacec@gmail.com`.
- **Phone** — `+91 70126 84869`, linked as `tel:+917012684869`.
- **Website** — `https://www.exodiacec.in`.
- **Links** — FOCES → `foces.ceconline.edu`, μLearn → `mulearn.org`, tile → `exodiacec.in`.

## Why a GIF and not SVG/CSS

Gmail and Outlook strip `<svg>`, `<style>` animations and `<canvas>`. An animated GIF
is the only format that still moves inside an inbox, so the IEDC tile is a ~40 KB GIF.
Frame 0 is the finished logo, so a client that never plays it (or a preview thumbnail)
still shows a complete mark; `iedc-static.png` is that same frame if you need a PNG.

The checker mark is a redraw in the IEDC/KSUM visual language, not the official artwork —
drop in the official PNG/GIF at `assets/iedc-animated.gif` to swap it wholesale.
