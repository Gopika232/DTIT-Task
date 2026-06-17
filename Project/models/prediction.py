import pickle
import os
class AttendancePredictor:
    def __init__(self):
        self.model = None
        self.encoder = None
        if os.path.exists("models/attendance_model.pkl"):
            self.model = pickle.load(
            open("models/attendance_model.pkl","rb"))
        if os.path.exists("models/label_encoder.pkl"):
            self.encoder = pickle.load(
            open("models/label_encoder.pkl","rb"))

    def predict(self,present_days):
        if self.model is None:
            return "Model not trained"

        result = self.model.predict([[present_days]])
        status = self.encoder.inverse_transform(result)

        return status[0]

predictor = AttendancePredictor()