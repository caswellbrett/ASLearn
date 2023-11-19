import os
import cv2
import string

DATA_PATH = './data'

sign_list = list(string.ascii_uppercase) + list(range(10))
dataset_size = 100

cap = cv2.VideoCapture(0)
for j in range(len(sign_list)):
    if not os.path.exists(os.path.join(DATA_PATH, str(sign_list[j]))):
        os.makedirs(os.path.join(DATA_PATH, str(sign_list[j])))

    print('Collecting data for class {}'.format(sign_list[j]))

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "' +
                    str(sign_list[j]) +
                    '" ! :)', (100, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord(str(sign_list[j]).lower()):
            break

    for i in range(dataset_size):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_PATH, 
                                 str(sign_list[j]), 
                                 '{}.jpg'.format(i)), 
                                 frame)


cap.release()
cv2.destroyAllWindows()