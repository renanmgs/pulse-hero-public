# Pulse Hero Public Site

Static landing page and store-compliance pages for Pulse Hero, served by GitHub
Pages at **https://pulsehero.charactercraftapp.com/**.

## Store listings

- App Store: https://apps.apple.com/us/app/pulse-hero-fitness-rpg/id6788211881
- Google Play: https://play.google.com/store/apps/details?id=app.fithero.fit_hero

## Pages

- `index.html` — landing page.
- `privacy-policy.html` — privacy policy (linked from both store listings).
- `delete-account.html` — public account deletion instructions.
- `404.html` — GitHub Pages serves this for any unmatched path, which is what
  gives `/e/<id>` partner-event links a landing page on static hosting.

## Files that must stay at the root

- `CNAME` — the custom domain.
- `.nojekyll` — stops Jekyll from stripping paths, notably `.well-known/`.
- `.well-known/assetlinks.json` — Android App Links verification.
- `app-ads.txt` — AdMob authorised sellers.
- `robots.txt`, `sitemap.xml` — indexing.

## Assets

`assets/shots/*.webp` are the real app screenshots, sourced from
`app/store_assets/source/provided_screenshots/` in the game repo.
`assets/og-cover.jpg` (1200×630) is the social-share card; it is generated from
the key art, not hand-designed, so regenerate it if the key art changes.

`assets/art/` is game art resized for the page — class crests, profession icons
and the exercise illustrations in the marquee. `tools/build-site-art.py`
generates it straight from `app/assets/images/` in the game repo, trimming the
transparent margins off the icons so they sit at the same optical size in a
grid. Re-run it after changing which exercises are picked, or after the game's
art changes:

```
python tools/build-site-art.py
```

The script hard-codes the game repo path at the top; edit it if the checkout
moves.

## Press kit

The press kit is **not** part of this repo — it is roughly 60 MB of
full-resolution source art, which does not belong in a GitHub Pages checkout.
It is assembled by `app/store_assets/build_press_kit.py` in the game repo and
distributed separately.

## Local preview

```
python -m http.server 4321
```

Note that `python -m http.server` does not serve `404.html` for unmatched paths,
so `/e/<id>` can only be tested by opening `/404.html` directly.

## GitHub Pages settings

- Source: `Deploy from a branch`
- Branch: `main`
- Folder: `/ (root)`
