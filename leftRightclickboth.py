import cv2
import time
import mediapipe as mp
import pyautogui


###################################
wCam , hCam= 1280, 720
##################################
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
middle_y=0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    middle_x = (screen_width/frame_width*x)
                    middle_y = (screen_height/frame_height*y)

                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = (screen_width/frame_width*x)
                    index_y = (screen_height/frame_height*y)

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = (screen_width/frame_width*x)
                    thumb_y = (screen_height/frame_height*y)
                    cv2.line(img=frame,(index_x, index_y), (thumb_x, thumb_y), (255, 0, 255))
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(0)
                    elif abs(index_y - middle_y) < 20:
                        pyautogui.rightClick()
                        pyautogui.sleep(0)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)
    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break