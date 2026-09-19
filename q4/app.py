from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("spam_model.joblib")

class Message(BaseModel):
    text: str

@app.get("/healthz", status_code = 200)
def health():
    return {"status": "ok",
            "version": "v2"}

@app.post("/predict")
def predict(message: Message):
    prediction = model.predict([message.text])[0]
    return {"label": prediction}