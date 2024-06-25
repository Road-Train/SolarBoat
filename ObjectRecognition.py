import cv2
import numpy as np
import pygetwindow as gw
from PIL import ImageGrab
import mediapipe as mp
from mediapipe.tasks.python import vision
import time

model_path = 'ssd_mobilenet_v2.tflite'
BaseOptions = mp.tasks.BaseOptions
ObjectDetector = mp.tasks.vision.ObjectDetector
ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Global variable to store the detection result
latest_detection_result = None

def print_result(result, image, timestamp_ms):
    global latest_detection_result
    latest_detection_result = result

options = ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    max_results=5,
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result,
    score_threshold=0.3,
    category_allowlist="boat"
)
detector = ObjectDetector.create_from_options(options)

def draw_bounding_boxes(image, detection_result):
    if detection_result is not None:
        for detection in detection_result.detections:
            bbox = detection.bounding_box
            start_point = (int(bbox.origin_x), int(bbox.origin_y))
            end_point = (int(bbox.origin_x + bbox.width), int(bbox.origin_y + bbox.height))
            cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
            
            label = detection.categories[0].category_name
            confidence = detection.categories[0].score
            text = f'{label} ({confidence:.2f})'
            cv2.putText(image, text, (start_point[0], start_point[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

def capture_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print(f"No window found with title: {window_title}")
        return
    
    window = windows[0]
    window.activate()

    while True:
        bbox = (window.left, window.top, window.right, window.bottom)
        screenshot = ImageGrab.grab(bbox=bbox)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Ensure the image is in RGB format
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
        frame_timestamp_ms = int(time.time() * 1000)  # Current time in milliseconds

        detector.detect_async(mp_image, frame_timestamp_ms)

        # Draw bounding boxes on the original image
        if latest_detection_result:
            draw_bounding_boxes(frame, latest_detection_result)

        cv2.imshow('Object Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    window_title = "Boat Simulation - Opera"  # Change this to your browser window's title
    capture_window(window_title)
