import cv2
import numpy as np

# Read in an image
image = cv2.imread("images/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)
# Display the original image
cv2.imshow('apollo',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

imageLine = image.copy()

# The line starts from (200,100) and ends at (400,100)
# The color of the line is YELLOW (Recall that OpenCV uses BGR format)
# Thickness of line is 5px
# Linetype is cv2.LINE_AA

cv2.line(imageLine, (200, 100), (400, 100), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA);

# Display the image
cv2.imshow('apollo',imageLine)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Draw a circle
imageCircle = image.copy()

cv2.circle(imageCircle, (900,500), 100, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA);

# Display the image
cv2.imshow('apollo',imageCircle)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a rectangle (thickness is a positive integer)
imageRectangle = image.copy()

cv2.rectangle(imageRectangle, (500, 100), (700,600), (255, 0, 255), thickness=5, lineType=cv2.LINE_8);

# Display the image
cv2.imshow('apollo',imageRectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

imageText = image.copy()
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2

cv2.putText(imageText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA);

# Display the image
cv2.imshow('apollo',imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()