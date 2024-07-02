import cv2
import numpy as np

def create_checkerboard(rows, cols, square_size, filename):
    checkerboard = np.zeros((rows * square_size, cols * square_size), dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                checkerboard[i * square_size:(i + 1) * square_size, j * square_size:(j + 1) * square_size] = 255
    cv2.imwrite(filename, checkerboard)

# Example usage
create_checkerboard(8, 12, 50, 'checkerboard.png')