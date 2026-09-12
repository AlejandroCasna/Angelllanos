from PIL import Image
import numpy as np

img = Image.open("assets/logo.png").convert("RGBA")
arr = np.array(img).astype(np.int16)

h, w = arr.shape[0], arr.shape[1]
corners = [arr[0, 0], arr[0, w - 1], arr[h - 1, 0], arr[h - 1, w - 1]]
bg = np.mean(corners, axis=0)[:3]
print("bg color:", bg)

rgb = arr[:, :, :3]
diff = np.sqrt(np.sum((rgb - bg) ** 2, axis=2))
print("max diff:", diff.max(), "min diff:", diff.min())

low, high = 12, 60
alpha = np.clip((diff - low) / (high - low), 0, 1) * 255
arr[:, :, 3] = alpha.astype(np.int16)

out = Image.fromarray(arr.astype(np.uint8), mode="RGBA")

bbox = out.getbbox()
print("bbox:", bbox)
pad = 20
if bbox:
    l, t, r, b = bbox
    l = max(0, l - pad)
    t = max(0, t - pad)
    r = min(w, r + pad)
    b = min(h, b + pad)
    out = out.crop((l, t, r, b))

out.save("assets/logo-transparent.png")
print("saved", out.size)
