from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import WorkoutSet as WorkoutSetModel

app = FastAPI()





@app.get("/")
def home():
    return {"message": "Welcome to GymOS!"}


@app.get("/hello")
def hello():
    return {"message": "GymOS API is working!"}


class WorkoutSet(BaseModel):
    exercise: str
    weight: float
    reps: int


@app.post("/sets")
def create_set(
    workout_set: WorkoutSet,
    db: Session = Depends(get_db)
):
    new_set = WorkoutSetModel(
        exercise=workout_set.exercise,
        weight=workout_set.weight,
        reps=workout_set.reps
    )

    db.add(new_set)
    db.commit()
    db.refresh(new_set)

    return {
        "message": "Workout set saved!",
        "data": new_set
    }


class WorkoutSetResponse(BaseModel):
    id: int
    exercise: str
    weight: float
    reps: int

    class Config:
        from_attributes = True

@app.get("/sets", response_model=list[WorkoutSetResponse])
def get_sets(db: Session = Depends(get_db)):
    return db.query(WorkoutSetModel).all()
