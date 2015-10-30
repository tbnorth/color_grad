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

A more complete example using it to color a map:
 * Get the maximum value for your DEM or other continuous variable grid:
```
gdalinfo score_category_NP_3857.tif | grep -i maximum
```
 * and then run the following Python code, capturing output in ``colors.txt``:
```python
from color_grad import ColorGrad  # https://github.com/tbnorth/color_grad

MAX = 0.72314321994781
cg = ColorGrad.from_ascii_ppm("gradient/ylw2brn.ppm")
cg.set_min_max(0, MAX)
alpha = 0
steps = 100
for step in range(steps):
    pos = float(step) / steps * MAX
    rgb = cg.rgb_int(pos)
    print pos, rgb[0], rgb[1], rgb[2], alpha
    alpha = 255
```
 * and finally make the colored map image:
```
gdaldem color-relief score_category_NP_3857.tif colors.txt -alpha -of png output.png
```
The `alpha` references cause the minimum value in the grid to be transparent.
