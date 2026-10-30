import cv2
image=input("Enter the name of the image file with extension: ")
# Load an image
image_path = input("Enter the image filename: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image. Check the filename and path.")
    raise SystemExit

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixels = image.reshape(-1, 3)
print(pixels.shape)
# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Display the image
    cv2.imshow("Clothing Image", image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()

    import matplotlib.pyplot as plt

plt.imshow(image)
plt.axis("off")  # Hide axes
plt.show()