import cv2
import sys
from topics.image_enhancement import main as enhance_image
from topics.image_compression import main as compress_image

# Input handling
if len(sys.argv) != 2:
	print("Please provide the path to the image")
	exit()
image_path = sys.argv[1]

# Read Image using OpenCV and initialize variables
image = cv2.imread(image_path)
image = cv2.resize(image,(500,500))
new_image = image.copy()
window_title = "Image"

# Get User Input for editing image
user_choice = input("How would you like to edit the image?\n1. Image Enhancement \n2. Image Compression\nEnter the number of your choice (1,2): ")

if user_choice == '1':
  new_image = enhance_image(image)
  window_title = "enhanced"
elif user_choice == '2':
# perform image compression, print Peak-signal-to-noise ratio (PSNR) and display the reconstructed image
  new_image = compress_image(image)
  window_title = "reconstructed"
else:
  print("Invalid option selected. Aborting...")
  exit()

# Display image (this part is very buggy. Apparently, it's hard for OpenCV to display images and close properly when there is user input after the close)
cv2.imshow("Original", image)
cv2.imshow(window_title.capitalize(), new_image)
cv2.waitKey()
cv2.destroyAllWindows()

# Save image
should_save = input("Would you like to save the image? (y/n): ")

if should_save.lower() == 'y':
	filename, extension = image_path.split(".")
	new_filename = f"{filename}_{window_title}.{extension}"
	cv2.imwrite(new_filename, new_image)
else:
  exit()