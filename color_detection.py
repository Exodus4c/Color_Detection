import cv2
import matplotlib.pyplot as plt


image_path = input("Enter the image filename or path: ").strip()

# OpenCV loads images in BGR format. If the path is invalid, it returns None.
image_bgr = cv2.imread(image_path)

if image_bgr is None:
    print("Could not load the image. Check that the filename and path are correct.")
    raise SystemExit(1)

# Convert to RGB for correct display with Matplotlib.
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# Each row contains one pixel as [red, green, blue].
pixels = image_rgb.reshape(-1, 3)
print("Pixel array shape:", pixels.shape)

plt.imshow(image_rgb)
plt.axis("off")
plt.show()
