import cv2
import numpy as np

def ext_ele (img_path = ".\media\cards.jpg"):

    img = cv2.imread(img_path)
    
    width, height = 250, 350
    pts1 = np.float32([[67, 486], [285, 360], [279, 745], [502, 604]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOut = cv2.warpPerspective(img, matrix, (width, height))

    cv2.imshow("output", imgOut)
    cv2.waitKey(0)


