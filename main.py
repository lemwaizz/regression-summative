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
    Age: int = Field(..., ge=0, description="Patient's age")
    Fever: int = Field(..., ge=0, le=1, description="Indicator for fever")
    Rash: int = Field(..., ge=0, le=1, description="Indicator for rash")
    Swollen_Lymph_Nodes: int = Field(..., ge=0, le=1, description="Indicator for swollen lymph nodes")
    Headache: int = Field(..., ge=0, le=1, description="Indicator for headache")
    Muscle_Aches: int = Field(..., ge=0, le=1, description="Indicator for muscle aches")
    Fatigue: int = Field(..., ge=0, le=1, description="Indicator for fatigue")
    Chills: int = Field(..., ge=0, le=1, description="Indicator for chills")
    Sore_Throat: int = Field(..., ge=0, le=1, description="Indicator for sore throat")
    Cough: int = Field(..., ge=0, le=1, description="Indicator for cough")
    Shortness_of_Breath: int = Field(..., ge=0, le=1, description="Indicator for shortness of breath")
    Nausea: int = Field(..., ge=0, le=1, description="Indicator for nausea")
    Vomiting: int = Field(..., ge=0, le=1, description="Indicator for vomiting")
    Diarrhea: int = Field(..., ge=0, le=1, description="Indicator for diarrhea")
    Skin_Lesions: int = Field(..., ge=0, le=1, description="Indicator for skin lesions")
    Travel_History: int = Field(..., ge=0, le=1, description="Indicator for recent travel history")
    Contact_with_Infected: int = Field(..., ge=0, le=1, description="Indicator for contact with infected person")
    Immunocompromised: int = Field(..., ge=0, le=1, description="Indicator for immunocompromised condition")

@app.post("/predict")
def predict(data: PredictionInput):
    try:
        input_features = np.array([[
            data.Age, data.Fever, data.Rash, data.Swollen_Lymph_Nodes, data.Headache,
            data.Muscle_Aches, data.Fatigue, data.Chills, data.Sore_Throat,
            data.Cough, data.Shortness_of_Breath, data.Nausea, data.Vomiting,
            data.Diarrhea, data.Skin_Lesions, data.Travel_History,
            data.Contact_with_Infected, data.Immunocompromised
        ]])
        prediction = model.predict(input_features)
        return {"Monkey Pox Diagnosis": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
