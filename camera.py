import cv2
from model import DiseasePredictor
from config import *

class CameraProcessor:

    def __init__(self):
        self.predictor = DiseasePredictor()
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        result_text = "No face detected"

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            result_text = self.predictor.analyze(face)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        return frame, result_text

    def generate_frames(self, camera):

        while True:
            success, frame = camera.read()
            if not success:
                break

            frame, result_text = self.process_frame(frame)

            cv2.putText(frame, result_text, TEXT_POSITION,
                        cv2.FONT_HERSHEY_SIMPLEX,
                        FONT_SCALE, COLOR, THICKNESS)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
