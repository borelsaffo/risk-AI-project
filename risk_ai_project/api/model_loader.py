import joblib, os
MODEL_PATH = os.path.join(os.path.dirname(__file__), "risk_model.joblib")
def load_model():
    return joblib.load(MODEL_PATH)
