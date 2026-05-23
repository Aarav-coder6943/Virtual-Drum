🥁 AIR DRUMS — Virtual Drum Kit Using Hand Tracking

Turn your webcam into a full-on virtual drum set using Computer Vision + Hand Tracking.
No expensive drum kit. No drum sticks. Just your hands, a webcam, and absolute chaos 🔥

This project uses MediaPipe Hands, OpenCV, and Pygame to detect hand movement and trigger drum sounds in real time.

✨ Features
✋ Real-time hand tracking
🥁 Virtual drum zones
⚡ Motion-based hit detection
🔊 Custom drum sounds
🎥 Webcam-powered interaction
🧠 Velocity-based strike recognition
🎨 Live visual interface with drum zones
🛠️ Tech Stack
Python
OpenCV
MediaPipe
Pygame
NumPy
📂 Project Structure
AIR-DRUMS/
│
├── sounds/
│   ├── snare.wav
│   ├── hihat.wav
│   ├── kick.wav
│   └── crash.wav
│
├── main.py
└── README.md
🚀 How It Works
1️⃣ Hand Tracking

The project uses MediaPipe Hands to detect and track hand landmarks in real time.

The system specifically tracks:

👆 Index finger tip (landmark[8])
2️⃣ Drum Zones

The webcam screen is divided into virtual drum regions:

Zone	Drum Sound
Left Bottom	Snare
Center Bottom	Hi-Hat
Right Bottom	Kick
Top Center	Crash

Each zone acts like an invisible drum pad.

3️⃣ Hit Detection

Instead of just checking position, the system detects downward velocity of your finger movement.

If movement speed exceeds a threshold:

velocity > 15

…it counts as a drum hit.

Honestly kinda cursed how well this works with just a webcam 😭

🎮 Controls
Key	Action
Q	Quit application
⚙️ Installation
Clone the Repository
git clone https://github.com/Aarav-coder6943/Virtual-Drum.git
cd Virtual-Drum
Install Dependencies
pip install opencv-python mediapipe pygame numpy
▶️ Usage

Run the project:

python drum_project.py

Make sure your webcam is connected.

🔊 Custom Sounds

You can replace the drum sounds with your own .wav files.

Supported sounds:

snare.wav
hihat.wav
kick.wav
crash.wav

Place them inside the sounds/ folder.

📸 Demo Features
Real-time hand landmark visualization
Interactive drum zones
Motion-triggered drum playback
Smooth webcam interface
🧠 Detection Logic

The system calculates vertical movement velocity:

velocity=previousY−currentY

Fast downward movement = drum hit.

📈 Future Improvements
🥁 Multi-hand support
🎵 Beat recording & playback
🎚️ Volume control using gestures
🎼 MIDI support
🌈 Better drum UI animations
🎧 Latency optimization
🕹️ VR / AR integration
🤖 AI-generated rhythm assistant
⚠️ Limitations
Requires decent lighting
Webcam FPS affects responsiveness
Fast movements may occasionally double-trigger
Background clutter can reduce tracking accuracy
💡 Inspiration

Inspired by rhythm games, motion tracking, and the idea of turning random computer vision projects into things that are actually stupidly fun to use.

Because why buy drums when your webcam can become one 💀

📜 License

This project is open-source under the MIT License.

🙌 Acknowledgements
Google
OpenCV
Pygame
⭐ Support

If this made you aggressively air-drum at 2 AM, give the repo a star ⭐
