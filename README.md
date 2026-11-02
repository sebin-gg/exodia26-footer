# Exodia '26 — email footer

Signature footer modelled on the reference design: italic *Thanks & Regards*, the IEDC
logo tile, a thin divider, then name / phone / website / email, with the FOCES and μLearn
marks in an "Organised by" row.

## Live assets

Images are served from GitHub Pages, so they work in a real inbox:

```
https://sebin-gg.github.io/exodia26-footer/assets/
```

Repo: <https://github.com/sebin-gg/exodia26-footer> (public, because free Pages requires it).
Re-push `assets/` if you ever replace a logo.

## Files

| File | What it is |
| --- | --- |
| `footer.html` | **Dark** footer — paste this into Gmail → Settings → Signature. |
| `footer-light.html` | **Light** twin for light/white mail clients. Same content, light card. |
| `preview.html`, `preview-light.png` … | Local look-checks with images inlined. Never paste these (Gmail strips data URIs). |
| `assets/` | `iedc-animated.gif`, `iedc-static.png`, `foces-dark.png`, `mulearn.png`, plus the official sources (`ref-iedc-dark.png`, `foces.svg`, `exodia.svg`). |
| `make_assets.py` | Regenerates the tile and logo files: `python make_assets.py`. |
| `ref/` | The WhatsApp reference video. |

## Details

- **Title** — EXODIA '26 / All Kerala Tech Gala
- **Phone** — `+91 70126 84869` → `tel:+917012684869`
- **Website** — `https://www.exodiacec.in`
- **Email** — `exodiacec@gmail.com`
- **Links** — FOCES → `foces.ceconline.edu`, μLearn → `mulearn.org`, tile → `exodiacec.in`

## The animated IEDC tile

The mark is cropped from the **official** IEDC lockup
(`innovate.startupmission.in/assets/im/iedcrecb.png`) — the diamond symbol only, because
the full lockup is 5:1 and unreadable at tile size.

It has to be a GIF: Gmail and Outlook strip `<svg>`, `<style>` animations and `<canvas>`,
so a GIF is the only thing that still moves in an inbox. Frame 0 is the finished logo, so
clients that never animate it — or a preview thumbnail — still show a complete mark.
`iedc-static.png` is that same frame as a PNG.

## Breaking gracefully

- Every `<img>` has real alt text naming the body, so blocked or unavailable images still
  say what they were (images-off Gmail, corporate proxies, host outage).
- Nothing meaningful lives inside an image: phone, site and email are live text links.
- Layout is nested tables, so clients that strip the `<style>` block keep the right order;
  the style block only adds mobile stacking below 480 px.
- A dead host costs you the logos, not the contact details.

## Logos

FOCES ships as a white mark, so `foces-dark.png` is a recolour for the light card and the
white pills. μLearn is used as supplied.
