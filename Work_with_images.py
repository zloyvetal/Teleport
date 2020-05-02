"""
This is a first file
"""
import cv2


img = cv2.imread('Ebalo.jpg', -1)
print(img)

cv2.imshow('image', img) #Show Img

k = cv2.waitKey(5000) #How much time we need to watch

# if we press "Esc" = close window
if k == 27:
    cv2.destroyAllWindows() #close window with img

# if we press S = save a new copy of img
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img) # create copy of img
    cv2.destroyAllWindows()




