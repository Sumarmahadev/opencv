import cv2
from matplotlib import pyplot as plt

image = cv2.imread("OIP.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert BGR to RGB for proper display in matplotlib
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis("off")
    plt.show()
else:
    print("ERROR: I could not change the color of image")
