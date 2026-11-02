# Exodia '26 — email footer

Signature footer modelled on the reference design: italic *Thanks & Regards*, the IEDC
logo tile, the small Exodia symbol beside the title, a thin divider, then name / phone /
website / email, with the FOCES and μLearn marks in an "Organised by" row.

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
| `paste-into-gmail.html` | **Copy from this.** Open in a browser, Ctrl+A, Ctrl+C, paste into Gmail → Settings → Signature. |
| `footer.html` | The dark footer source, for pasting into a mailer/HTML editor. |
| `footer-light.html` | Light twin for light/white mail clients. |
| `preview.png`, `preview-light.png` | Rendered look-checks (images inlined as base64 — never paste these). |
| `assets/` | `iedc-animated.gif`, `iedc-static.png`, `foces-dark.png`, `mulearn.png`, `exodia-mark.png`, plus sources. |
| `make_assets.py` | Regenerates the tile and logo files: `python make_assets.py`. |
| `ref/` | The WhatsApp reference video. |

## Details

- **Title** — EXODIA '26 / All Kerala Tech Gala, with the Exodia symbol beside it
- **Phone** — `+91 70126 84869` → `tel:+917012684869`
- **Website** — `https://www.exodiacec.in`
- **Email** — `exodiacec@gmail.com`
- **Links** — FOCES → `foces.ceconline.edu`, μLearn → `mulearn.org`, tile → `exodiacec.in`

## Weight budget (under 40 KB)

| Asset | Size |
| --- | --- |
| `iedc-animated.gif` (208 px, 24 colours, 6 frames) | 15.6 KB |
| `mulearn.png` (175×48) | 7.5 KB |
| `exodia-mark.png` (56×56) | 4.2 KB |
| `foces-dark.png` (186×40) | 3.1 KB |
| **images** | **30.4 KB** |
| markup (comments stripped) | 7.1 KB |
| **total** | **37.5 KB** |

The wide wordmarks were the surprise cost: μLearn shipped at 1578×396 / 33 KB for an
18 px logo. Everything is now sized at roughly 2× its display size.

## The animated IEDC tile

The mark is cropped from the **official** IEDC lockup
(`innovate.startupmission.in/assets/im/iedcrecb.png`) — the diamond symbol only, because
the full lockup is 5:1 and unreadable at tile size.

It has to be a GIF: Gmail and Outlook strip `<svg>`, `<style>` animations and `<canvas>`,
so a GIF is the only thing that still moves in an inbox. Frame 0 is the finished logo, so
clients that never animate it — or a preview thumbnail — still show a complete mark.
`iedc-static.png` is that same frame as a PNG.

The Exodia symbol is rasterised from `exodia.svg` with headless Chrome, because mail
clients will not render SVG either.

## Breaking gracefully

- Every `<img>` has real alt text naming the body, so blocked or unavailable images still
  say what they were (images-off Gmail, corporate proxies, host outage).
- Nothing meaningful lives inside an image: phone, site and email are live text links.
- Layout is nested tables, so clients that strip the `<style>` block keep the right order;
  the style block only adds mobile stacking below 480 px.
- Card backgrounds are set with both `bgcolor` and inline `background-color`, so the dark
  card survives Gmail's signature editor and Outlook.
