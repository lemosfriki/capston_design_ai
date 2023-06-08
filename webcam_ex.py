import cv2
import keyboard
import os
from ultralytics import YOLO

num = 0
file_name = ""

webcam = cv2.VideoCapture(0)

model_path = "best.pt"
model = YOLO(model_path)
threshold = 0.7
class_name_dict = {0: 'shoes'}

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.imshow("test", frame)

webcam.release()
cv2.destroyAllWindows()
