Place an animated GIF to enable the hero animation in the README.

Steps:
1. Prepare a GIF named `hero.gif` (recommended size: 600x338 or similar, max ~1-2 MB).
2. Optimize the GIF with ImageMagick (optional):

```bash
# Resize and optimize
magick convert input.gif -coalesce -resize 600x -layers Optimize assets/hero.gif
```

3. Put `assets/hero.gif` in the repository root path `dr-arobase/assets/hero.gif`.
4. Commit and push. The README will automatically display the animated GIF.

If you want, send me the GIF and I can optimize and add it for you.