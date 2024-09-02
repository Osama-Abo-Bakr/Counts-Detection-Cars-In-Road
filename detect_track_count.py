import cv2
import pandas as pd
from ultralytics import YOLO
import time
from tracker import *


model = YOLO('yolov8s.pt')
class_name = model.names
video = cv2.VideoCapture(r'D:\Courses language programming\7_Computer Vision\Computer Vision - Full Course\6-Object Detection\Speed-detection-of-vehicles-main\highway_mini.mp4')

tracker = Tracker()
red_line_y = 198
blue_line_y = 268
offset = 6

down = {}
up = {}
counter_down = []
counter_up = []


while True:
    ret, image = video.read()
    w, h, _ = image.shape
    if not ret:
        break

    image = cv2.resize(image, (1020, 500))
    result = model.predict(image)[0].boxes.data
    px = pd.DataFrame(result).astype(float)

    list_box = []
    for index, row in px.iterrows():
        x1, y1, x2, y2, confidence, cls = int(row[0]), int(row[1]), int(row[2]), int(row[3]), row[4], class_name[int(row[5])]
        if cls == 'car':
            list_box.append([x1, y1, x2, y2,])

    boxes_id = tracker.update(list_box)
    for box in boxes_id:
        x3, y3, x4, y4, id = box
        cy = (y3 + y4) // 2
        cx = (x3 + x4) // 2

        # Going Down
        if (cy - offset) < red_line_y < (cy + offset):
            down[id] = time.time()
        if id in down:
            if (cy - offset) < blue_line_y < (cy + offset):
                elapsed_time = time.time() - down[id]
                if counter_down.count(id) == 0:
                    counter_down.append(id)
                    cv2.circle(image, (cx, cy), 4, (0, 0, 255), -1)
                    cv2.rectangle(image, (x3, y3), (x4, y4), (0, 255, 0), 2)  # Draw bounding box

        if (cy - offset) < blue_line_y < (cy + offset):
            up[id] = time.time()
        if id in up:
            if (cy - offset) < red_line_y < (cy + offset):
                elapsed1_time = time.time() - up[id]
                if counter_up.count(id) == 0:
                    counter_up.append(id)
                    cv2.circle(image, (cx, cy), 4, (0, 0, 255), -1)
                    cv2.rectangle(image, (x3, y3), (x4, y4), (0, 255, 0), 2)  # Draw bounding box

    cv2.rectangle(image, (w//2-150, 0), (w//2+100, 40), (0, 255, 255), -1)
    cv2.putText(image, 'Count & Detection Car', (w//2-130, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    red_color = (0, 0, 255)
    blue_color = (255, 0, 0)
    green_color = (0, 255, 0)
    text_color = (0, 0, 0)

    cv2.line(image, (172, 198), (774, 198), red_color, 3)  # starting cordinates and end of line cordinates
    cv2.putText(image, 'red line', (172, 198), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1, cv2.LINE_AA)
    cv2.line(image, (8, 268), (927, 268), blue_color, 3)  # seconde line
    cv2.putText(image, 'blue line', (8, 268), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1, cv2.LINE_AA)

    cv2.rectangle(image, (0, 0), (200, 90), (0, 255, 255), -1)
    cv2.putText(image, ('Going Down - ' + str(len(counter_down))), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color,
                1, cv2.LINE_AA)
    cv2.putText(image, ('Going Up - ' + str(len(counter_up))), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1,
                cv2.LINE_AA)

    cv2.imshow("frames", image)
    if cv2.waitKey(1) == ord('o'):
        break


video.release()
cv2.destroyAllWindows()