import cv2 
import numpy as np

def create_change_highlights(img_one, img_two):
    gray_one = cv2.cvtColor(img_one, cv2.COLOR_BGR2GRAY)
    gray_two = cv2.cvtColor(img_two, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray_one, gray_two)
    
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)

    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)


    highlighted = img_two.copy()
    highlighted[thresh == 255] = [0, 0, 255] # [Blue, Green, Red]

    return highlighted