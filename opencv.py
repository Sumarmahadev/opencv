
#image loading
import cv2

image=cv2.imread('OIP.jpg')
#for diplaying the imges
#if image is  not None:
   #cv2.imshow("image showing",image)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
#else:
   # print("cound not found")

#saveing the images
if image is  not None:
   succuss=cv2.imwrite("output_python.png",image)
   if succuss:
      print("Image succusfully saved as the 'output_python.png'")
   else:
      print("Failed to save an image")
      
else:
   print("Error:could not load image")