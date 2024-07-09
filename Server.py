import asyncio
import base64
import io
import numpy as np
import websockets
import json
from PIL import Image
from ObjectRecognition import ObjectRecognition
from DisparityMap import DisparityMap
from CollisionAvoidance import CollisionAvoidance

# Starts a small server at localhost:8765
# This server is used to connect the simulation to the logic.
# You will need to run this BEFORE starting the simulation in order for the program to receive input.

detector = ObjectRecognition()
disparity_map = DisparityMap()
collision_avoidance = CollisionAvoidance()

# Buffers to hold incoming image chunks
center_image_chunks = []
left_image_chunks = []
right_image_chunks = []
center_total_chunks = 0
left_total_chunks = 0
right_total_chunks = 0

async def process_images(websocket, path):
    global center_image_chunks, left_image_chunks, right_image_chunks, center_total_chunks, left_total_chunks, right_total_chunks
    try:
        while True:
            # Turning chunks into whole images.
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
            else:
                if index == 0:
                    center_image_chunks = []
                    center_total_chunks = total
                center_image_chunks.append(chunk)

                if len(center_image_chunks) == center_total_chunks:
                    center_image_data = ''.join(center_image_chunks)
                    center_image_data = base64.b64decode(center_image_data + '=' * (-len(center_image_data) % 4))
                    center_image = Image.open(io.BytesIO(center_image_data))
                    center_image = np.array(center_image)
                    center_image_chunks = []
            # 
            if 'center_image' in locals() and 'left_image' in locals() and 'right_image' in locals():
                detections = detector.detect(center_image)
                disparity, depth_map = disparity_map.compute(left_image, right_image)
                action = collision_avoidance.decide(detections, depth_map, disparity)
                await websocket.send(json.dumps({"action": action}))

    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")

async def main():
    server = await websockets.serve(process_images, "localhost", 8765, max_size=1024**3)
    print("Server started at ws://localhost:8765")
    await server.wait_closed()

asyncio.get_event_loop().run_until_complete(main())
