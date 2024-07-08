import mediapipe as mp
import time
import cv2
# Object Recognition class. Takes a livestream, and returns a detections object.
# Access the detections via 'last_detection_result.detections'
class ObjectRecognition:
    def __init__(self):
        self.model_path = 'ssd_mobilenet_v2.tflite'
        BaseOptions = mp.tasks.BaseOptions
        ObjectDetector = mp.tasks.vision.ObjectDetector
        ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
        VisionRunningMode = mp.tasks.vision.RunningMode
        self.latest_detection_result = None
        def print_result(result, image, timestamp_ms):
            self.latest_detection_result = result
        
        self.options = ObjectDetectorOptions(
            base_options=BaseOptions(model_asset_path=self.model_path),
            max_results=5,
            running_mode=VisionRunningMode.LIVE_STREAM,
            result_callback=print_result,
            score_threshold=0.3
        )
        self.detector = ObjectDetector.create_from_options(self.options)

    def detect(self, image):
        image_format = mp.ImageFormat.SRGB
        frame_timestamp_ms = int(time.time() * 1000)  # Current time in milliseconds
        rgbImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mpImage = mp.Image(image_format, data=rgbImage)
        
        self.detector.detect_async(mpImage, frame_timestamp_ms)
        if self.latest_detection_result is not None:
            return self.latest_detection_result
