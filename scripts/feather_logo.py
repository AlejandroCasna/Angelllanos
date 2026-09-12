from PIL import Image
import numpy as np

img = Image.open("assets/logo-crop.png").convert("RGBA")
arr = np.array(img).astype(np.float32)
h, w = arr.shape[:2]

yy, xx = np.mgrid[0:h, 0:w]

feather = 0.16  # fraction of dimension used for fade
fx = np.clip(np.minimum(xx, w - 1 - xx) / (w * feather), 0, 1)
fy = np.clip(np.minimum(yy, h - 1 - yy) / (h * feather), 0, 1)
falloff = np.minimum(fx, fy)
# smoothstep
falloff = falloff * falloff * (3 - 2 * falloff)

arr[:, :, 3] = arr[:, :, 3] * falloff

out = Image.fromarray(arr.astype(np.uint8), mode="RGBA")
out.save("assets/logo-header.png")
print("saved", out.size)
