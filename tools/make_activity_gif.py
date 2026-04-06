#!/usr/bin/env python3
import io, sys, math
try:
    from PIL import Image, ImageEnhance
except Exception as e:
    print('Pillow not installed:', e)
    raise
try:
    import requests
except Exception as e:
    print('requests not installed:', e)
    raise

def make_gif(url, outpath, frames_count=10, duration=120):
    print('Downloading', url)
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    img = Image.open(io.BytesIO(r.content)).convert('RGBA')
    frames = []
    for i in range(frames_count):
        # brightness pulse
        factor = 1.0 + 0.08 * math.sin(2 * math.pi * i / frames_count)
        enhancer = ImageEnhance.Brightness(img)
        frame = enhancer.enhance(factor).convert('P', palette=Image.ADAPTIVE)
        frames.append(frame)

    frames[0].save(outpath, save_all=True, append_images=frames[1:], duration=duration, loop=0, optimize=True)
    print('Saved', outpath)


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://github-readme-activity-graph.vercel.app/graph?username=dr-arobase&theme=tokyo-night&hide_border=true&area=true&bg_color=0D1117&color=58A6FF&line=58A6FF&point=FF6B6B&area_color=1E3A5F'
    out = sys.argv[2] if len(sys.argv) > 2 else '../assets/activity-anim.gif'
    make_gif(url, out)
