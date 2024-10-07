import cv2
import numpy as np

image = cv2.imread("Logo.png") # Reading the 'logo.png' file and loading it into the 'image' variable.
imageBlackWhite = cv2.imread("Logo.png",0) # Loading the 'Logo.png' image in grayscale mode (0 flag converts it to black and white).

cv2.imshow("this is logo",image) # Opening a window to display the loaded image.
cv2.imshow("this is logo",imageBlackWhite)

cv2.imwrite("NewImage.png",imageBlackWhite) # Saving the black and white image as 'NewImage.png'.

cv2.waitKey(0) # Waits for a key press to prevent the window from closing immediately.
cv2.destroyAllWindows() # Closes all OpenCV windows.