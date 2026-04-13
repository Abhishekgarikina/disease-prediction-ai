import cv2
import numpy as np

class DiseasePredictor:

    def __init__(self):
        self.dark_threshold = 70
        self.bright_threshold = 180

    def preprocess(self, face):
        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        return cv2.GaussianBlur(gray, (5, 5), 0)

    def extract_features(self, image):
        brightness = np.mean(image)
        variance = np.var(image)
        return brightness, variance

    def classify(self, brightness, variance):

        if brightness < self.dark_threshold:
            return "Fatigue / Dark Circles Detected"
        
        elif brightness > self.bright_threshold:
            return "Healthy Skin"
        
        elif variance > 5000:
            return "Possible Acne / Skin Irregularity"
        
        elif 100 < brightness < 150:
            return "Normal Condition"
        
        else:
            return "Mild Skin Variation"

    def analyze(self, face):
        processed = self.preprocess(face)
        brightness, variance = self.extract_features(processed)
        return self.classify(brightness, variance)
