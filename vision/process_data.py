import os
import pickle

import mediapipe as mp
import cv2

DATA_PATH = "./data"

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True, 
                       min_detection_confidence = 0.3)

coords = []
sign_type = []

for letter_dir in os.listdir(DATA_PATH)[:2]:
    for img_file in os.listdir(os.path.join(DATA_PATH, letter_dir))[:1]:
        data_temp = []
        x_coords = []
        y_coords = []

        img = cv2.imread(os.path.join(DATA_PATH, letter_dir, img_file))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_coords.append(x)
                    y_coords.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_temp.append(x - min(x_coords))
                    data_temp.append(y - min(y_coords))

            coords.append(data_temp)
            sign_type.append(letter_dir)

f = open('data.pickle', 'wb')
pickle.dump({'coords': coords, 'sign_type':sign_type}, f)
f.close()