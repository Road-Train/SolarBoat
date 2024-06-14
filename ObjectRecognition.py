import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
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
    score_threshold=0.5
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

def process_webcam():
    global latest_detection_result
    video = cv2.VideoCapture(0)
    
    if not video.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        success, image = video.read()

        if not success:
            break

        # Ensure the image is in RGB format
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
        frame_timestamp_ms = int(time.time() * 1000)  # Current time in milliseconds

        detector.detect_async(mp_image, frame_timestamp_ms)

        # Draw bounding boxes on the original image
        if latest_detection_result:
            draw_bounding_boxes(image, latest_detection_result)

        cv2.imshow('Object Detection', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_webcam()
