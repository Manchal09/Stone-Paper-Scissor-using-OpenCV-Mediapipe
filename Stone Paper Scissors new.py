import cv2
import mediapipe as mp
import random
import numpy as np
import time   # ADDED for cooldown

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Game choices
choices = ["rock", "paper", "scissors"]

# Score variables (ADDED)
user_score = 0
computer_score = 0

# Cooldown (ADDED)
last_time = 0
cooldown = 5  # seconds

# Define function to recognize hand gestures
def recognize_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    # Calculate distances
    distance_thumb_index = abs(thumb_tip.x - index_tip.x)
    distance_index_middle = abs(index_tip.y - middle_tip.y)
    
    # Rock: All fingers closed
    if distance_thumb_index < 0.05 and distance_index_middle < 0.05:
        return "rock"
    
    # Paper: All fingers open
    elif all(landmarks[i].y < landmarks[i-2].y for i in [8, 12, 16, 20]):
        return "paper"
    
    # Scissors: Only index and middle fingers open
    elif all(landmarks[i].y < landmarks[i-2].y for i in [8, 12]) and all(landmarks[i].y > landmarks[i-2].y for i in [16, 20]):
        return "scissors"

    return None

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    user_choice = None

    # ALWAYS track hand continuously (no change)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            user_choice = recognize_gesture(hand_landmarks.landmark)

    # Cooldown: Only accept a move once every 5 sec
    if user_choice and time.time() - last_time > cooldown:

        last_time = time.time()   # reset cooldown

        computer_choice = random.choice(choices)
        result_text = f"You: {user_choice} | Computer: {computer_choice}"

        # Determine winner
        if user_choice == computer_choice:
            winner = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            winner = "You win! 🎉"
            user_score += 1     # ADD score
        else:
            winner = "You lose! 😢"
            computer_score += 1  # ADD score

    # -------- DISPLAY TEXT (ONLY SMALL FONT CHANGES) --------

    # Score at TOP (Yellow)
    cv2.putText(frame, f"Score: You {user_score} - {computer_score} Computer",
                (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Result (Blue)
    if "result_text" in locals():
        cv2.putText(frame, result_text, (50, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Winner/Loser (Green)
    if "winner" in locals():
        cv2.putText(frame, winner, (50, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Cooldown timer display
    remain = cooldown - (time.time() - last_time)
    if remain > 0:
        cv2.putText(frame, f"Next move in: {int(remain)}s",
                    (50, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)

    # Show frame
    cv2.imshow("Rock Paper Scissors - Hand Gesture", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()