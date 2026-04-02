# 🎨 Air Canvas (Hand Gesture Drawing System)

A Python-based **Virtual Drawing System** that allows you to draw in the air using your fingers.

This project uses **hand tracking and gesture recognition** to create a touchless painting experience.

---

# 🚀 Features

✔ Draw in air using finger gestures
✔ Multiple colors (Blue, Green, Red)
✔ Eraser tool
✔ Gesture-based mode switching
✔ Smooth real-time drawing
✔ Clear canvas with keyboard shortcut

---

# 🛠 Technologies Used

* Python
* OpenCV
* MediaPipe (Hand Tracking)
* NumPy

---

# 📂 Project Structure

```id="p8m3xt"
air-canvas-hand-gesture
│
├── main.py
└── README.md
```

👉 Rename your file to **main.py** for clean structure.

---

# ⚙️ Installation

1️⃣ Install Python 3.x

2️⃣ Install required libraries:

```bash id="r3n7kl"
pip install opencv-python mediapipe numpy
```

---

# ▶️ How to Run

```bash id="k9p2zl"
git clone https://github.com/ravigautam7739/air-canvas-hand-gesture.git
cd air-canvas-hand-gesture
python main.py
```

---

# 🧠 How It Works

1. Webcam captures live video
2. MediaPipe detects hand landmarks
3. Finger positions are tracked
4. System detects gestures:

👉 ✌️ **Two fingers up → Selection Mode**

* Choose color (Blue / Green / Red)
* Select eraser

👉 ☝️ **One finger up → Drawing Mode**

* Draw on screen using finger movement

5. Drawing is stored on a virtual canvas and merged with video

---

# 💻 Controls

| Gesture / Key  | Action                |
| -------------- | --------------------- |
| ✌️ Two Fingers | Select Color / Eraser |
| ☝️ One Finger  | Draw                  |
| `C` Key        | Clear Canvas          |
| `ESC` Key      | Exit                  |

---

# 💻 Example Output

```id="q2m7vr"
User moves finger →

Drawing appears on screen

Switch to 2 fingers →

Select RED color

Continue drawing
```

---

# 🎯 Use Cases

* Virtual whiteboard
* Gesture-based interfaces
* Touchless drawing apps
* Education tools
* AI/Computer Vision demos

---

# ⚠️ Notes

* Requires webcam
* Works best in good lighting
* Keep hand clearly visible
* May need calibration for accuracy

---

# 🔮 Future Improvements

* Save drawings as images
* Add more colors and tools
* Multi-hand support
* Shape recognition (circle, rectangle)
* GUI enhancements

---

# ⭐ Support

If you found this project interesting, give it a **star ⭐**.

---

# 📱 Follow for More Projects

I regularly share **Python, AI, and computer vision projects**.

Stay tuned 🚀
