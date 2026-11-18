"""Turn a 1080x1350 poster into a 1080x1920 Instagram story image.
Usage: python3 make_story.py poster.jpg out.jpg "#topcolor" "#bottomcolor"
"""
import sys
from PIL import Image, ImageDraw, ImageFilter
src, out, c1, c2 = sys.argv[1:5]
def hx(c): c=c.lstrip('#'); return tuple(int(c[i:i+2],16) for i in (0,2,4))
W,H=1080,1920
a,b=hx(c1),hx(c2)
bg=Image.new('RGB',(W,H))
d=ImageDraw.Draw(bg)
for y in range(H):
    t=y/(H-1); d.line([(0,y),(W,y)],fill=tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3)))
p=Image.open(src).convert('RGB')
w=1000; h=round(p.height*w/p.width); p=p.resize((w,h),Image.LANCZOS)
x=(W-w)//2; y=(H-h)//2
sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([x+6,y+16,x+w+6,y+h+16],28,fill=(0,0,0,110))
sh=sh.filter(ImageFilter.GaussianBlur(18)); bg.paste(sh,(0,0),sh)
m=Image.new('L',(w,h),0); ImageDraw.Draw(m).rounded_rectangle([0,0,w,h],28,fill=255)
bg.paste(p,(x,y),m)
bg.save(out,'JPEG',quality=92)
