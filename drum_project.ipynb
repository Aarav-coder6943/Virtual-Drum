import cv2
import mediapipe as mp
import pygame
import numpy as np
import time

# ---------- AUDIO ----------
pygame.mixer.init()
snare = pygame.mixer.Sound("sounds/snare.wav")
hihat = pygame.mixer.Sound("sounds/hihat.wav")
kick = pygame.mixer.Sound("sounds/kick.wav")
crash = pygame.mixer.Sound("sounds/crash.wav")

# ---------- HAND TRACKING ----------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# ---------- CAMERA ----------
cap = cv2.VideoCapture(0)

prev_y = 0
cooldown = 0.15  # seconds
last_hit = time.time()

# ---------- DRUM ZONES ----------
def draw_zone(img, x1, y1, x2, y2, label):
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
    cv2.putText(img, label, (x1 + 10, y1 + 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    # Define zones
    zones = {
        "snare": (0, int(h*0.6), int(w*0.33), h),
        "hihat": (int(w*0.33), int(h*0.6), int(w*0.66), h),
        "kick":  (int(w*0.66), int(h*0.6), w, h),
        "crash": (int(w*0.33), 0, int(w*0.66), int(h*0.3))
    }

    for z, (x1,y1,x2,y2) in zones.items():
        draw_zone(img, x1, y1, x2, y2, z.upper())

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark[8]  # index finger tip
            x, y = int(lm.x * w), int(lm.y * h)

            cv2.circle(img, (x, y), 10, (0, 255, 0), -1)

            velocity = prev_y - y
            prev_y = y

            now = time.time()
            if velocity > 15 and (now - last_hit) > cooldown:
                if zones["snare"][0] < x < zones["snare"][2] and zones["snare"][1] < y < zones["snare"][3]:
                    snare.play()
                    last_hit = now
                elif zones["hihat"][0] < x < zones["hihat"][2] and zones["hihat"][1] < y < zones["hihat"][3]:
                    hihat.play()
                    last_hit = now
                elif zones["kick"][0] < x < zones["kick"][2] and zones["kick"][1] < y < zones["kick"][3]:
                    kick.play()
                    last_hit = now
                elif zones["crash"][0] < x < zones["crash"][2] and zones["crash"][1] < y < zones["crash"][3]:
                    crash.play()
                    last_hit = now

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("AIR DRUMS 🥁", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
