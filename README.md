# Facial_Analysis

A real-time facial analysis tool built with **Python**, **OpenCV**, and **DeepFace**.  
This project detects faces from a webcam feed and displays the **dominant age, gender, race, and emotion** in real time with a clean, readable overlay.

---

## Table of Contents
- [Project Overview](#project-overview)  
- [Recording](#recording)  
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

## Recording
You can view a demo below:  


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
