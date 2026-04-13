from flask import Flask, render_template, Response
import cv2
from camera import CameraProcessor
from config import *

app = Flask(__name__)

camera = cv2.VideoCapture(CAMERA_INDEX)
processor = CameraProcessor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(processor.generate_frames(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/health')
def health():
    return {"status": "AI system running"}

if __name__ == "__main__":
    app.run(debug=DEBUG)
