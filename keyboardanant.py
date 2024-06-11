import cv2
import numpy as np
import pyautogui
                                                           
# Function to perform keyboard actions based on hand gestures
def perform_action(action):
    if action == "fist":
        pyautogui.press('space') # Simulate pressing the spacebar
    elif action == "one_finger":
        pyautogui.press('up') # Simulate pressing the up arrow key
    elif action == "two_fingers":
        pyautogui.press('down') # Simulate pressing the down arrow key
    elif action == "three_fingers":
        pyautogui.press('left') # Simulate pressing the left arrow key
    elif action == "four_fingers":
        pyautogui.press('right') # Simulate pressing the right arrow key

# Function to detect and recognize hand gestures
def detect_hand_gesture(hand):
    # Implement your gesture recognition logic here
    # You can use hand landmarks or other techniques to recognize different gestures
    # For simplicity, let's assume we have already detected the number of fingers raised
    
    # Detect number of fingers raised
    num_fingers = 0
    # Your logic to count the number of fingers raised

    # Map the number of fingers raised to corresponding gestures
    if num_fingers == 0:
        return "fist"
    elif num_fingers == 1:
        return "one_finger"
    elif num_fingers == 2:
        return "two_fingers"
    elif num_fingers == 3:
        return "three_fingers"
    elif num_fingers == 4:
        return "four_fingers"

# Main function to capture video feed and detect hand gestures
def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply a threshold to the grayscale frame
        _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Find contours in the thresholded frame
        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if any contours are found
        if contours:
            # Find the contour with the maximum area
            contour = max(contours, key=cv2.contourArea)

            # Calculate the convex hull of the contour
            hull = cv2.convexHull(contour)

            # Draw the contour and convex hull on the frame
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            cv2.drawContours(frame, [hull], -1, (0, 0, 255), 2)

            # Detect hand gesture
            gesture = detect_hand_gesture(hull)

            # Perform the corresponding action based on the detected gesture
            perform_action(gesture)

        # Display the frame
        cv2.imshow("Hand Gesture Recognition", frame)

        # Check for 'q' key to exit the program
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the video capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Run the main function
if __name__ == '__main__':
    main()