import cv2

image = cv2.imread('./test.JPG',cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(500,500))

# Display image
cv2.imshow('image',image)
cv2.waitKey()