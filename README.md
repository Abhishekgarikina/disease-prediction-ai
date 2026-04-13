# AI-Based Disease Prediction using Facial Characteristics

## Overview
This project is a real-time AI-based facial analysis system that detects facial features using a webcam and predicts possible health conditions.

The system uses computer vision techniques to analyze facial patterns and simulate disease prediction.

## Features
- Real-time face detection using OpenCV
- Live webcam integration
- Multi-condition prediction (fatigue, acne, normal, healthy)
- Modular and scalable architecture
- Web interface using Flask (HTML, CSS, JavaScript)

## Technologies Used
- Python
- Flask
- OpenCV
- NumPy
- HTML, CSS, JavaScript

## Project Structure
- app.py → Main application
- camera.py → Handles video streaming
- model.py → AI prediction logic
- config.py → Configuration settings
- templates/ → Frontend HTML
- static/ → CSS and JavaScript

## How It Works
1. The system captures real-time video using a webcam.
2. Face detection is performed using OpenCV.
3. Facial features are analyzed using image processing techniques.
4. The system predicts possible conditions based on extracted features.
5. Results are displayed live on the screen.

## How to Run
```bash
pip install -r requirements.txt
python app.py