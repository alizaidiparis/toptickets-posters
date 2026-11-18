import sys
from playwright.sync_api import sync_playwright
html, outdir, dur, fps = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4])
times = [float(t) for t in sys.argv[5].split(',')] if len(sys.argv)>5 else None
import os; os.makedirs(outdir, exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto("file://"+os.path.abspath(html)); pg.wait_for_timeout(800)
    pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
    ts = times or [i/fps for i in range(int(dur*fps))]
    for i,t in enumerate(ts):
        pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={t*1000})")
        pg.screenshot(path=f"{outdir}/f{i:04d}.jpg", type="jpeg", quality=90)
    b.close()
