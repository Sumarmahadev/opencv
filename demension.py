
#demension
import cv2
image=cv2.imread("OIP.jpg")

if image is not None:
    h,w,c=image.shape
    print(f"Image Loaded:\nHeight:{h}\nwidth:{w}\nChannels:{c}")
else:
    print("could not load image")