import numpy as np
import cv2
# Takes in detections, a depth map and a disparity map and calculates the action the boat should take.
class CollisionAvoidance:
    def __init__(self):
        self.f = 1.0  # Focal length (replace with actual value)
        self.B = 10.0  # Baseline distance (same units as your Three.js scene)
        self.start_point = None
        self.end_point = None
    def decide(self, detections, depth_map, disparity):
        if detections is not None:
            for obj in detections.detections:
                bbox = obj.bounding_box
                self.start_point = (int(bbox.origin_x), int(bbox.origin_y))
                self.end_point = (int(bbox.origin_x + bbox.width), int(bbox.origin_y + bbox.height))

                # Avoid division by zero
                valid_disparity = disparity[self.start_point[1]:self.end_point[1], self.start_point[0]:self.end_point[0]] > 0
                valid_disparity_values = disparity[self.start_point[1]:self.end_point[1], self.start_point[0]:self.end_point[0]][valid_disparity]
                
                if valid_disparity_values.size > 0:
                    depth_values = (self.f * self.B) / valid_disparity_values
                    depth_map[self.start_point[1]:self.end_point[1], self.start_point[0]:self.end_point[0]][valid_disparity] = depth_values

            # Temporary to see if the script still runs. Delete this when you actually start using it for logic.
            if np.max(depth_map) > 0:
                cv2.imshow("Depth Map", depth_map / np.max(depth_map))
            else:
                cv2.imshow("Depth Map", depth_map)
            cv2.waitKey(1)

            # This is where the logic should be that makes the boat move.
            action = "no_action"
            if np.any(depth_map[self.start_point[1]:self.end_point[1], self.start_point[0]:self.end_point[0]][valid_disparity] < 1.0):  # Arbitrary threshold
                action = "avoid"
            
            return action
