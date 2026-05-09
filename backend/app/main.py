from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.prediction_controller import router as prediction_router
from app.controllers.report_controller import router as report_router

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prediction_router)
app.include_router(report_router)

@app.get("/")
def home():
    return {
        "message": "AI API Running"
    }