import cv2
import numpy as np
from PIL import ImageGrab

liness = []

def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=100, threshold2=110)
    processed_image = cv2.GaussianBlur(processed_image, (5, 5), 0)
    return processed_image

def get_road(image, points):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, points, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def find_lines(image):
    minLineLength = 120
    maxLineGap = 50
    lines = cv2.HoughLinesP(image, 1, np.pi/180, 180, minLineLength, maxLineGap)
    return lines

def draw_lines(image, lines):
    minLineLength = 120
    maxLineGap = 50
    lines = cv2.HoughLinesP(road, 1, np.pi/180, 180, minLineLength, maxLineGap)
    if lines is None:
        return
    for line in lines:
        coords = line[0]
        cv2.line(image, (coords[0], coords[1]), (coords[2], coords[3]), (0,255,0), 2)
    return

while True:
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    img = process_image(screen)
    points = np.array([[10, 500], [10, 450], [300, 300], [500, 300], [800, 450], [800, 500]])
    road = get_road(img, [points])

    lines = find_lines(road)
    draw_lines(screen, lines)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    cv2.imshow('game', screen)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
