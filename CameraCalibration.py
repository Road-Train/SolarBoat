import cv2
import numpy as np
import glob

# Prepare object points (3D points in real world space)
checkerboard_size = (7, 7)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
square_size = 1.0  # The size of a square in your defined unit (e.g., meters)
objp = np.zeros((checkerboard_size[0] * checkerboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:checkerboard_size[0], 0:checkerboard_size[1]].T.reshape(-1, 2)*square_size

# Arrays to store object points and image points from all images
objpoints = []  # 3d point in real world space
imgpoints_left = []  # 2d points in image plane for the left camera

# Load images
images_left = glob.glob('calibration/left/*.png')

for img_left in images_left:
    img_l = cv2.imread(img_left)
    gray_l = cv2.cvtColor(img_l, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret_l, corners_l = cv2.findChessboardCorners(gray_l, checkerboard_size, None)

    # If found, add object points, image points (after refining them)
    if ret_l:
        objpoints.append(objp)
        corners2_l = cv2.cornerSubPix(gray_l, corners_l, (11, 11), (-1, -1),criteria)
        imgpoints_left.append(corners2_l)

# Calibrate the left camera
ret, mtx_left, dist_left, rvecs_left, tvecs_left = cv2.calibrateCamera(objpoints, imgpoints_left, gray_l.shape[::-1], None, None)

# Save the left camera calibration data
print(mtx_left, dist_left)
np.savez('calibration_data_left.npz', mtx=mtx_left, dist=dist_left)
# Arrays to store object points and image points from all images
imgpoints_right = []  # 2d points in image plane for the right camera

# Load images
images_right = glob.glob('calibration/right/*.png')

for img_right in images_right:
    img_r = cv2.imread(img_right)
    gray_r = cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret_r, corners_r = cv2.findChessboardCorners(gray_r, checkerboard_size, None)

    # If found, add object points, image points (after refining them)
    if ret_r:
        corners2_r = cv2.cornerSubPix(gray_r, corners_r, (11, 11), (-1, -1),criteria)
        imgpoints_right.append(corners2_r)

# Calibrate the right camera
ret, mtx_right, dist_right, rvecs_right, tvecs_right = cv2.calibrateCamera(objpoints, imgpoints_right, gray_r.shape[::-1], None, None)

# Save the right camera calibration data
np.savez('calibration_data_right.npz', mtx=mtx_right, dist=dist_right)
