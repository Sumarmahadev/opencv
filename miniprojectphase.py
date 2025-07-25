import cv2 

# Step 1: Ask user for image file name or load the image by user input
user = input("Enter the image file name (e.g. image.jpg): ")
image = cv2.imread(user)

# Step 2: Check if image is found
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Step 3: Convert to grayscale

    
    cv2.imshow("Grayscale Image", gray) # Step 4: Show the grayscale image
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 5: Ask if user wants to save the grayscale image
    save_options = input("Do you want to save the grayscale image? (yes/no): ").lower()
    
    if save_options == "yes":
        output_name = input("Enter the output filename (e.g. output.jpg): ")
        cv2.imwrite(output_name, gray)  #here we saves the as as user name with that coverted  image
        print(f"Image saved as {output_name}")
    else:
        print("Image not saved.")
else:
    print("Error: Image not found. Please check the file name or path.")
