import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

# Load pre-calibrated parameters
stereo_params = {
    'left_camera_matrix': np.array([[...]]) , # Fill in with your values
    'right_camera_matrix': np.array([[...]]) ,# Fill in with your values
    'left_distortion': np.array([...]) , # Fill in with your values
    'right_distortion': np.array([...]) ,# Fill in with your values
    'R': np.array([[...]]), # Rotation matrix between the cameras
    'T': np.array([[...]]), # Translation vector between the cameras
}

# Stereo rectification (Adjust as per your calibration results)
R1, R2, P1, P2, Q, _, _ = cv2.stereoRectify(
    stereo_params['left_camera_matrix'], stereo_params['left_distortion'],
    stereo_params['right_camera_matrix'], stereo_params['right_distortion'],
    (640, 480), stereo_params['R'], stereo_params['T'])

map1x, map1y = cv2.initUndistortRectifyMap(
    stereo_params['left_camera_matrix'], stereo_params['left_distortion'], R1, P1, (640, 480), cv2.CV_16SC2)
map2x, map2y = cv2.initUndistortRectifyMap(
    stereo_params['right_camera_matrix'], stereo_params['right_distortion'], R2, P2, (640, 480), cv2.CV_16SC2)

# Initialize stereo block matching object
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

# Object detection setup
model_path = 'ssd_mobilenet_v2.tflite'
BaseOptions = mp.tasks.BaseOptions
ObjectDetector = mp.tasks.vision.ObjectDetector
ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
VisionRunningMode = mp.tasks.vision.RunningMode

latest_detection_result = None

def print_result(result, image, timestamp_ms):
    global latest_detection_result
    latest_detection_result = result

options = ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    max_results=5,
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result,
    score_threshold=0.5
)
detector = ObjectDetector.create_from_options(options)

def draw_bounding_boxes(image, detection_result, disparity, Q):
    if detection_result is not None:
        for detection in detection_result.detections:
            bbox = detection.bounding_box
            start_point = (int(bbox.origin_x), int(bbox.origin_y))
            end_point = (int(bbox.origin_x + bbox.width), int(bbox.origin_y + bbox.height))
            cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
            
            label = detection.categories[0].category_name
            confidence = detection.categories[0].score
            text = f'{label} ({confidence:.2f})'
            
            # Estimate distance
            center_x = int(bbox.origin_x + bbox.width / 2)
            center_y = int(bbox.origin_y + bbox.height / 2)
            disparity_value = disparity[center_y, center_x]
            if disparity_value > 0:  # Avoid division by zero
                distance = Q[2, 3] / (disparity_value + 1e-6)  # Small epsilon to avoid division by zero
                text += f' Distance: {distance:.2f}m'
            
            cv2.putText(image, text, (start_point[0], start_point[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Capture video from two cameras
cap_left = cv2.VideoCapture(0)
cap_right = cv2.VideoCapture(1)

while cap_left.isOpened() and cap_right.isOpened():
    ret_left, frame_left = cap_left.read()
    ret_right, frame_right = cap_right.read()
    
    if not ret_left or not ret_right:
        break

    # Rectify images
    rectified_left = cv2.remap(frame_left, map1x, map1y, cv2.INTER_LINEAR)
    rectified_right = cv2.remap(frame_right, map2x, map2y, cv2.INTER_LINEAR)

    # Convert to grayscale
    gray_left = cv2.cvtColor(rectified_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(rectified_right, cv2.COLOR_BGR2GRAY)

    # Compute disparity
    disparity = stereo.compute(gray_left, gray_right)

    # Normalize disparity map for visualization
    disp_vis = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    disp_vis = np.uint8(disp_vis)

    # Convert rectified_left to RGB and feed it to the detector
    rectified_left_rgb = cv2.cvtColor(rectified_left, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rectified_left_rgb)
    frame_timestamp_ms = int(time.time() * 1000)  # Current time in milliseconds

    detector.detect_async(mp_image, frame_timestamp_ms)

    # Draw bounding boxes on the rectified left image
    if latest_detection_result:
        draw_bounding_boxes(rectified_left, latest_detection_result, disparity, Q)

    # Display images
    cv2.imshow('Disparity Map', disp_vis)
    cv2.imshow('Object Detection', rectified_left)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()
