import cv2
import mediapipe as mp
import pickle
import numpy as np
import sys

# parsing args
if len(sys.argv) == 2:
    word_to_sign = sys.argv[1]
else:
    raise Exception("Bad number of arguments")

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True, 
                       min_detection_confidence = 0.3)

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

word_to_sign = word_to_sign.replace('0', 'O')
word_to_sign = word_to_sign.replace('1', 'D')
word_to_sign = word_to_sign.replace('2', 'V')
word_to_sign = word_to_sign.replace('6', 'W')

while word_to_sign != "":
    data_temp = []
    x_coords = []
    y_coords = []

    ret, frame = cap.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
            
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
        if len(data_temp) == 42:
            prediction = model.predict([np.asarray(data_temp)])

        if prediction[0] == word_to_sign[:1]:
            print(prediction[0])
            word_to_sign = word_to_sign[1:]
    cv2.imshow('frame', frame)
    cv2.waitKey(5)

cap.release()
cv2.destroyAllWindows()