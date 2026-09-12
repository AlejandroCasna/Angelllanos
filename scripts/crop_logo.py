from PIL import Image
import numpy as np

img = Image.open("assets/logo.png").convert("RGB")
arr = np.array(img).astype(np.int16)
h, w = arr.shape[:2]

luminance = arr[:, :, 0] * 0.299 + arr[:, :, 1] * 0.587 + arr[:, :, 2] * 0.114
mask = luminance > 75

ys, xs = np.where(mask)
print("text pixels:", len(xs))
l, r = xs.min(), xs.max()
t, b = ys.min(), ys.max()
print("raw bbox:", l, t, r, b)

pad_x = int((r - l) * 0.22)
pad_y = int((b - t) * 0.35)
l = max(0, l - pad_x)
r = min(w, r + pad_x)
t = max(0, t - pad_y)
b = min(h, b + pad_y)
print("padded bbox:", l, t, r, b)

cropped = img.crop((l, t, r, b))
cropped.save("assets/logo-crop.png")
print("saved size", cropped.size)

corners = [cropped.getpixel((0, 0)), cropped.getpixel((cropped.width - 1, 0)),
           cropped.getpixel((0, cropped.height - 1)), cropped.getpixel((cropped.width - 1, cropped.height - 1))]
print("crop corners:", corners)
