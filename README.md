# Facial_Analysis

A real-time facial analysis tool built with **Python**, **OpenCV**, and **DeepFace**.  
This project detects faces from a webcam feed and displays the **dominant age, gender, race, and emotion** in real time with a clean, readable overlay.

---

## Table of Contents
- [Project Overview](#project-overview)  
- [Demo](#demo)  
- [Features](#features)  
- [Installation](#installation)  
- [Built With](#built-with)  

---

## Project Overview
This project uses **DeepFace** for deep learning–based facial attribute analysis and **OpenCV** for real-time webcam capture.  
It processes every few frames in a **background thread** to keep the video feed smooth, then overlays analysis results directly on the video.

If no face is detected, the tool clearly displays `"No Face Detected"`.  
Text output has a **black outline** for readability against any background.

---

## Demo
You can view a demo below:  
<img width="636" height="507" alt="Screenshot 2025-08-12 at 2 35 54 PM" src="https://github.com/user-attachments/assets/72bfd1e3-f7a0-4df6-922f-d731ae609ea0" />

<img width="701" height="559" alt="Screenshot 2025-08-12 at 2 36 17 PM" src="https://github.com/user-attachments/assets/c486bb21-9f80-4c81-981b-ec25e897f5b1" />



---

## Features
- Real-time **age, gender, race, and emotion** detection from webcam
- Smooth performance using threaded analysis
- Readable on-screen text with black outline for contrast
- Automatic handling of “No Face Detected” case
- Works with macOS and Windows webcam sources
- Uses **only the most recent frame** for analysis to prevent lag

---

## Built With
- **Python 3.10**
- OpenCv — Webcam capture & drawing
- DeepFace — Facial attribute analysis
- Threading — Background processing for smooth video

---

## Installation

### Prerequisites
- Python 3.10
- Webcam (internal or external)
- macOS
- Virtual environment (recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/facial-analysis.git
cd facial-analysis

# Create and activate virtual environment
python3 -m venv deepface-env
source deepface-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### To run
```bash
python3 main.py
```
Press q to quit the webcam feed
