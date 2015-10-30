# color_grad
Pick colors from a color gradient. Python 2.7 and 3.x

Found this useful for many projects coloring maps etc.  Simple workflow:
 * create an simple rectangular image with a horizontal gradient using Inkscape, Gimp, etc.
 * Rescale it 1 pixel high by approximately the width you exported at, e.g.:
```
# graphicsmagick commands...
mogrify -resize '!130x!1' red2ylw2blu.png
```
 * then convert to an *ascii* ppm:
```
convert -quality 0 red2ylw2blu.png red2ylw2blu.ppm
```
 * and now you can use it in Python:
```python
from color_grad import ColorGrad

cg = ColorGrad.from_ascii_ppm("gradient/ylw2brn.ppm")
cg.set_min_max(0, 0.5)
print(cg.rgb_int(0.1), cg.rgb_int(0.4), cg.rgb_int(0.6))
```
yields ``(229, 204, 0) (153, 53, 0) (128, 2, 0)``.
