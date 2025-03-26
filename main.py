from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load best performing model
model = joblib.load("knn_model.pkl")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input data schema
class PredictionInput(BaseModel):
    Rectal_Pain: int = Field(..., ge=0, le=1, description="Patient's age")
    Sore_Throat: int = Field(..., ge=0, le=1, description="Indicator for fever")
    Penile_Oedema: int = Field(..., ge=0, le=1, description="Indicator for rash")
    Solitary_Leision: int = Field(..., ge=0, le=1, description="Indicator for swollen lymph nodes")
    Swollen_Tonsils: int = Field(..., ge=0, le=1, description="Indicator for headache")
    HIV_Infection: int = Field(..., ge=0, le=1, description="Indicator for muscle aches")
    STI: int = Field(..., ge=0, le=1, description="Indicator for fatigue")
    Systemic_Illness_Fever: int = Field(..., ge=0, le=1, description="Indicator for chills")
    Systemic_Illness_Muscle_Aches_and_Pain: int = Field(..., ge=0, le=1, description="Indicator for sore throat")
    Systemic_Illness_Swollen_Lymph_Nodes: int = Field(..., ge=0, le=1, description="Indicator for cough")
    Target: int = Field(..., ge=0, le=1, description="Indicator for fatigue")
@app.post("/predict")
def predict(data: PredictionInput):
    try:
        input_features = np.array([[
            data.Rectal_Pain, data.Sore_Throat, data.Penile_Oedema, data.Solitary_Leision, data.Swollen_Tonsils,
            data.HIV_Infection, data.STI, data.Systemic_Illness_Fever, data.Systemic_Illness_Muscle_Aches_and_Pain,
            data.Systemic_Illness_Swollen_Lymph_Nodes, data.Target
        ]])
        prediction = model.predict(input_features)
        return {"Monkey Pox Diagnosis": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
