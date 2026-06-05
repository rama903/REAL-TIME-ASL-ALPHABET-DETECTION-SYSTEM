import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("asl_model.h5")

labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

cap = cv2.VideoCapture(0)

word = ""
last_prediction = ""
frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    roi = frame[100:300, 100:300]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    _, thresh = cv2.threshold(
        blur,
        120,
        255,
        cv2.THRESH_BINARY
    )

    img = cv2.resize(thresh, (64,64))

    img = img.astype("float32") / 255.0

    img = img.reshape(1,64,64,1)

    prediction = model.predict(img, verbose=0)

    letter = labels[np.argmax(prediction)]

    if letter == last_prediction:
        frame_count += 1
    else:
        frame_count = 0
        last_prediction = letter

    if frame_count > 50:
        word += letter
        frame_count = 0

    cv2.rectangle(
        frame,
        (100,100),
        (300,300),
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Prediction: {letter}",
        (10,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Word: {word}",
        (10,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2
    )

    cv2.imshow("ASL Detection", frame)

    cv2.imshow("Threshold", thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
