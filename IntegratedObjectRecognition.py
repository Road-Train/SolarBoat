import json
import cv2
import numpy as np
import websockets
import asyncio
import base64
from PIL import Image
import io
import mediapipe as mp
from mediapipe.tasks.python import vision
import time
# Old object detection script, takes the left and right boat camera's inputs and shows a depth map.
# Not deleted for demonstration purposes.
# Define camera parameters
f = 1.0  # Focal length (replace with actual value)
B = 10.0  # Baseline distance (same units as your Three.js scene)
model_path = 'ssd_mobilenet_v2.tflite'
BaseOptions = mp.tasks.BaseOptions
ObjectDetector = mp.tasks.vision.ObjectDetector
ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
VisionRunningMode = mp.tasks.vision.RunningMode
latest_detection_result_left = None
latest_detection_result_right = None
def print_result(result, image, timestamp_ms):
    global latest_detection_result_left
    global latest_detection_result_right
    if(image == mp_left):
        latest_detection_result_left = result
    else:
        latest_detection_result_right = result
options = ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    max_results=1,
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result,
    score_threshold=0.3
)
left_detector = ObjectDetector.create_from_options(options)
right_detector = ObjectDetector.create_from_options(options)
# Buffers to hold incoming image chunks
left_image_chunks = []
right_image_chunks = []
left_total_chunks = 0
right_total_chunks = 0
async def process_images(websocket, path):
    global left_image_chunks, right_image_chunks, left_total_chunks, right_total_chunks
    global latest_detection_result_left
    global latest_detection_result_right
    global mp_left
    global mp_right
    try:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            cameraId = data['cameraId']
            chunk = data['chunk']
            index = data['index']
            total = data['total']
            if cameraId == 'left':
                if index == 0:
                    left_image_chunks = []
                    left_total_chunks = total
                left_image_chunks.append(chunk)

                if len(left_image_chunks) == left_total_chunks:
                    left_image_data = ''.join(left_image_chunks)
                    left_image_data = base64.b64decode(left_image_data + '=' * (-len(left_image_data) % 4))
                    left_image = Image.open(io.BytesIO(left_image_data))
                    left_image = np.array(left_image)
                    left_image_chunks = []

            elif cameraId == 'right':
                if index == 0:
                    right_image_chunks = []
                    right_total_chunks = total
                right_image_chunks.append(chunk)

                if len(right_image_chunks) == right_total_chunks:
                    right_image_data = ''.join(right_image_chunks)
                    right_image_data = base64.b64decode(right_image_data + '=' * (-len(right_image_data) % 4))
                    right_image = Image.open(io.BytesIO(right_image_data))
                    right_image = np.array(right_image)
                    right_image_chunks = []
            if 'left_image' in locals() and 'right_image' in locals():
                # Convert to grayscale
                gray_left = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
                gray_right = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

                # Convert to RGB
                rgb_left = cv2.cvtColor(left_image, cv2.COLOR_BGR2RGB)
                rgb_right = cv2.cvtColor(right_image, cv2.COLOR_BGR2RGB)

                # convert to MP
                image_format=mp.ImageFormat.SRGB
                frame_timestamp_ms = int(time.time() * 1000)  # Current time in milliseconds
                mp_left = mp.Image(image_format,data=rgb_left)
                mp_right = mp.Image(image_format,data=rgb_right)
                left_detector.detect_async(mp_left,frame_timestamp_ms)
                right_detector.detect_async(mp_right,frame_timestamp_ms)
                
                # Compute disparity map
                stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
                disparity = stereo.compute(gray_left, gray_right).astype(np.float32) / 16.0
                valid_disparity_mask = disparity > 0
                depth_map = np.zeros_like(disparity)
                if latest_detection_result_right is not None:
                    for obj in latest_detection_result_right.detections:
                        bbox = obj.bounding_box
                        start_point = (int(bbox.origin_x), int(bbox.origin_y))
                        end_point = (int(bbox.origin_x + bbox.width), int(bbox.origin_y + bbox.height))
                        depth_map[start_point[1]:end_point[1], start_point[0]:end_point[0]] = (f * B) / disparity[start_point[1]:end_point[1], start_point[0]:end_point[0]]
                cv2.imshow("Depth Map", depth_map / np.max(depth_map))
                cv2.waitKey(1)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")

async def main():
    # server = await websockets.serve(process_images, "localhost", 8765, max_size=1024**3)
    print("This is an old file, run Server.py instead.")
    # await server.wait_closed()

# asyncio.get_event_loop().run_until_complete(main())
