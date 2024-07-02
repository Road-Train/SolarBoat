import cv2
import numpy as np
import math

import cv2

def find_keypoints_and_descriptors(image):
    # Use ORB detector for example
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return keypoints, descriptors

def match_keypoints(desc1, desc2):
    # Use BFMatcher to find matches
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc1, desc2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

def compute_disparity(left_image, right_image):
    # Convert to grayscale
    gray_left = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

    # Create StereoBM object
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(gray_left, gray_right)
    
    return disparity


# Load images
left_image = cv2.imread('calibration/left/left_camera_image_6.png')
right_image = cv2.imread('calibration/right/right_camera_image_6.png')

# Detect keypoints and descriptors
kp1, desc1 = find_keypoints_and_descriptors(left_image)
kp2, desc2 = find_keypoints_and_descriptors(right_image)

# Match keypoints
matches = match_keypoints(desc1, desc2)

# Draw matches for visualization
img_matches = cv2.drawMatches(left_image, kp1, right_image, kp2, matches, None)
cv2.imshow('Matches', img_matches)
cv2.waitKey(0)

# Compute disparity map
disparity = compute_disparity(left_image, right_image)

def reconstruct_3d(disparity, left_image, camera_matrix, dist_coeffs, baseline):
    # Get the shape of the image
    h, w = left_image.shape[:2]
    
    # Create Q matrix for 3D reconstruction
    Q = np.float32([[1, 0, 0, -w / 2.0],
                    [0, -1, 0, h / 2.0],
                    [0, 0, 0, -camera_matrix[0, 0]],
                    [0, 0, 1 / baseline, 0]])
    
    # Reproject image to 3D
    points_3d = cv2.reprojectImageTo3D(disparity, Q)
    
    # Mask out points with invalid disparity
    mask = disparity > disparity.min()
    
    return points_3d, mask
fov = 75
aspect = 1879/970
near = 1
far = 1000
focalLength = 1 / math.tan(fov*math.pi/360)
fx = focalLength * aspect  # Focal length in pixels (x-axis)
fy = focalLength  # Focal length in pixels (y-axis)
cx = aspect/2   # Principal point (x-axis)
cy = 0.5   # Principal point (y-axis)
k1 = 0.1   # Radial distortion coefficient
k2 = 0.01  # Radial distortion coefficient
p1 = 0.001 # Tangential distortion coefficient
p2 = -0.002  # Tangential distortion coefficient
k3 = 0.001  # Radial distortion coefficient
# Load camera parameters (assume these are already calibrated)
camera_matrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
dist_coeffs = np.array([k1, k2, p1, p2, k3])
baseline = 0.1  # Example baseline in meters

# Reconstruct 3D points
points_3d, mask = reconstruct_3d(disparity, left_image, camera_matrix, dist_coeffs, baseline)

# Filter valid points
valid_points = points_3d[mask]

# Visualize points (optional)
for point in valid_points:
    x, y, z = point
    print(f'Point: ({x}, {y}, {z})')

cv2.destroyAllWindows()