import cv2
import numpy as np
# Generates a disparity map from 2 adjacent cameras
# Baseline is the distance the pair of cameras are apart, in centimeters.
# YOU WILL NEED TO RE-CALCULATE THESE VALUES FOR THE REAL BOAT.
class DisparityMap:
    def __init__(self):
        self.focalLength = 1.0  
        self.baseline = 10.0  

    def compute(self, left_image, right_image):
        gray_left = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
        gray_right = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)
        stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
        disparity = stereo.compute(gray_left, gray_right).astype(np.float32) / 16.0
        depth_map = np.zeros_like(disparity)
        
        return disparity, depth_map
