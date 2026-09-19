from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import redis

app = FastAPI()

model = joblib.load("spam_model.joblib")

cache = redis.Redis(
    host="redis-server",
    port=6379,
    decode_responses=True
)

class Message(BaseModel):
    text: str

@app.get("/healthz", status_code = 200)
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(message: Message):
    cached_label = cache.get(message.text)
    if cached_label is not None:
        return {
            "label": cached_label,
            "cache":"hit"
                }

    prediction = model.predict([message.text])[0]

    cache.setex(message.text, 600, prediction)

    return {"label": prediction, "cache":"miss"}