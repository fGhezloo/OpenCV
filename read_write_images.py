import cv2

# Read image, flag 0=grayscale 1=colored  -1=unchanged with alpha channel
img = cv2.imread('lena.jpg', -1)

# print(img)

# Displays image img in window imageWindow
cv2.imshow('imageWindow', img)

# waits 5000 miliseconds before closing the window
cv2.waitKey(5000)

# closes window
cv2.destroyWindow('imageWindow')


cv2.imwrite('lena_copy.png', img)
