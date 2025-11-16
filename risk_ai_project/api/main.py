from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib, numpy as np, os

app = FastAPI(title="Risk Scoring API")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "risk_model.joblib")
model = joblib.load(MODEL_PATH)

class Features(BaseModel):
    vuln_score: float
    criticalite: float
    exposition: int
    historique_incident: float

@app.post("/scoring")
def scoring(features: Features):
    try:
        X = np.array([[
            features.vuln_score,
            features.criticalite,
            features.exposition,
            features.historique_incident
        ]])
        prob = float(model.predict_proba(X)[0][1])
        score = round(prob * float(features.criticalite), 4)
        return { "probability": prob, "score_risque": score }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
