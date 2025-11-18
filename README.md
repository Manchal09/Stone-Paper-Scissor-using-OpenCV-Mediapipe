# Stone-Paper-Scissor-using-OpenCV-Mediapipe
This project is a real-time Rock–Paper–Scissors game built using OpenCV and MediaPipe, designed to recognize hand gestures through a webcam and let the user play against the computer. The system uses MediaPipe Hands to detect 21 landmark points on the user’s hand, allowing accurate recognition of three gestures: Rock, Paper, and Scissors. Based on the detected gesture, the computer randomly selects its move, and the result is displayed instantly along with a continuously updated score.
To ensure fair gameplay, a 5-second cooldown timer is implemented after each detected move. This prevents continuous unintended gesture detection and gives time to set the next gesture properly. Meanwhile, hand landmark tracking remains active at all times, giving a smooth visual experience and helping the user understand how the system interprets hand positions.
The project showcases the integration of computer vision, machine learning–based hand tracking, and real-time interaction, making it an excellent beginner-friendly CV/AI project. It can be extended further with UI improvements, gesture animations, sound effects, and enhanced gesture models.

✨ Key Features
1. Real-time webcam feed using OpenCV
2. Continuous hand landmark tracking using MediaPipe
3. Rock, Paper, Scissors gesture detection based on 21 hand landmarks
4. Live visual feedback with color-coded text
5. Automatic computer move generation
6. Dynamic score tracking
7. 5-second cooldown to avoid repeated accidental detection
8. Clean, simple interface with minimal code changes from original

📁 Use Cases
Gesture-controlled games
Human-computer interaction projects
Computer vision learning projects
AI-based gesture recognition demos
Academic mini-project / portfolio project

🧠 Tech Stack
Python
OpenCV for image processing and webcam handling
MediaPipe for hand landmark detection and gesture recognition
NumPy for numerical operations
