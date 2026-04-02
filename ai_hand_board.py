import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

# Canvas
canvas = None

# Colors
colors = {
    "BLUE": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "RED": (0, 0, 255),
    "ERASER": (0, 0, 0)
}

color = colors["BLUE"]
brush_thickness = 5
eraser_thickness = 30

xp, yp = 0, 0


def fingers_up(hand_landmarks):
    """Detect which fingers are up"""
    lm = hand_landmarks.landmark

    fingers = []

    # Index finger
    fingers.append(lm[8].y < lm[6].y)
    # Middle finger
    fingers.append(lm[12].y < lm[10].y)

    return fingers


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    # ===== UI BAR =====
    cv2.rectangle(frame, (0, 0), (640, 80), (40, 40, 40), -1)

    cv2.putText(frame, "BLUE", (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, colors["BLUE"], 2)
    cv2.putText(frame, "GREEN", (180, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, colors["GREEN"], 2)
    cv2.putText(frame, "RED", (340, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, colors["RED"], 2)
    cv2.putText(frame, "ERASE", (470, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            lm = handLms.landmark

            h, w, _ = frame.shape

            x1, y1 = int(lm[8].x * w), int(lm[8].y * h)   # Index
            x2, y2 = int(lm[12].x * w), int(lm[12].y * h) # Middle

            fingers = fingers_up(handLms)

            # ✌️ Selection Mode (2 fingers)
            if fingers[0] and fingers[1]:
                xp, yp = 0, 0

                if y1 < 80:
                    if 40 < x1 < 140:
                        color = colors["BLUE"]
                    elif 180 < x1 < 300:
                        color = colors["GREEN"]
                    elif 340 < x1 < 440:
                        color = colors["RED"]
                    elif 470 < x1 < 600:
                        color = colors["ERASER"]

            # ☝️ Drawing Mode (only index finger)
            elif fingers[0] and not fingers[1]:
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1

                thickness = eraser_thickness if color == colors["ERASER"] else brush_thickness

                cv2.line(canvas, (xp, yp), (x1, y1), color, thickness)
                xp, yp = x1, y1

    # Merge canvas and frame
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    cv2.imshow("Virtual Painter", frame)

    key = cv2.waitKey(1)

    # ESC to exit
    if key == 27:
        break

    # Press 'c' to clear canvas
    if key == ord('c'):
        canvas = np.zeros_like(frame)

cap.release()
cv2.destroyAllWindows()