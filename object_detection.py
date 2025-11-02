import os
import cv2
import time
import pyttsx3
from ultralytics import YOLO

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

# Load YOLO model
model = YOLO('yolov8n.pt')

# Config
SPEAK_INTERVAL = 5  # seconds between speech updates
last_spoken_time = 0
last_sentence = ""

def speak(text):
    try:
        engine.stop()  # cancel any ongoing speech
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)

def detect_objects():
    global last_spoken_time, last_sentence
    cap = cv2.VideoCapture(0)
    print("Object Detection with Voice started...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)
        current_time = time.time()
        detected_labels = set()

        for result in results[0].boxes.data.cpu().numpy():
            x1, y1, x2, y2, score, class_id = result
            class_id = int(class_id)
            label = model.names[class_id]
            conf = float(score)

            detected_labels.add(label)

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Build sentence from detected objects
        if detected_labels:
            sentence = ", ".join(detected_labels) + " detected"
            if (current_time - last_spoken_time > SPEAK_INTERVAL) and (sentence != last_sentence):
                print(sentence)
                speak(sentence)
                last_spoken_time = current_time
                last_sentence = sentence

        cv2.imshow("Object Speaker Detection", frame)

        if (cv2.waitKey(1) & 0xFF == ord('q')) or cv2.getWindowProperty("Object Speaker Detection", cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()
    engine.stop()

if __name__ == "__main__":
    detect_objects()
