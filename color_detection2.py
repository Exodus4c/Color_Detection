import cv2
from tkinter import Tk, filedialog
from matplotlib import pyplot as plt
import sys

# Set a compatible backend for matplotlib (fixes crashes on some systems)
import matplotlib
matplotlib.use('TkAgg')  # Use the Tkinter backend

# Function to open a file dialog and select an image
def upload_image():
    try:
        # Hide the root window
        Tk().withdraw()
        
        # Open a file dialog to select an image
        image_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
        )
        
        # Check if a file was selected
        if not image_path:
            print("No file selected. Exiting...")
            return None
        
        return image_path
    except Exception as e:
        print(f"Error in upload_image(): {e}")
        return None

# Main function
def main():
    try:
        # Ask the user to upload an image
        image_path = upload_image()
        
        if image_path:
            # Load the image
            image = cv2.imread(image_path)
            
            # Check if the image was loaded successfully
            if image is None:
                print("Error: Could not load image. Please check the file path.")
            else:
                # Convert from BGR to RGB (OpenCV loads images in BGR format)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                
                # Display the image using matplotlib
                plt.imshow(image)
                plt.axis("off")  # Hide axes
                plt.title("Uploaded Image")
                plt.show()
    except Exception as e:
        print(f"Error in main(): {e}")

# Run the program
if __name__ == "__main__":
    main()