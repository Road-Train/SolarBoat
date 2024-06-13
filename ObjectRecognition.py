import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import os

model_path = 'ssd_mobilenet_v2.tflite'
BaseOptions = mp.tasks.BaseOptions
ObjectDetector = mp.tasks.vision.ObjectDetector
ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    max_results=5,
    running_mode=VisionRunningMode.VIDEO
)
detector = ObjectDetector.create_from_options(options)

def draw_bounding_boxes(image, detection_result):
    for detection in detection_result.detections:
        bbox = detection.bounding_box
        start_point = (int(bbox.origin_x), int(bbox.origin_y))
        end_point = (int(bbox.origin_x + bbox.width), int(bbox.origin_y + bbox.height))
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
        
        label = detection.categories[0].category_name
        confidence = detection.categories[0].score
        text = f'{label} ({confidence:.2f})'
        cv2.putText(image, text, (start_point[0], start_point[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

def FrameCapture(frame_freq,imgPath):
    video = cv2.VideoCapture(imgPath)
    success, image = video.read()

    fps = int(video.get(cv2.CAP_PROP_FPS))
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    print('FPS:', fps)
    print('Extracting every {} frames'.format(frame_freq))
    print('Total Frames:', length)
    print('Number of Frames Saved:', (length // frame_freq) + 1)

    count = 0
    success = 1

    while count < length:
        video.set(cv2.CAP_PROP_POS_FRAMES, count)
        success, image = video.read()

        if not success:
            break

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        frame_timestamp_ms = int(1000 * count / fps)

        detection_result = detector.detect_for_video(mp_image, frame_timestamp_ms)

        draw_bounding_boxes(image, detection_result)

        cv2.imshow('Object Detection', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        count += frame_freq

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    FrameCapture(1)
