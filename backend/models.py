from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Numeric, Integer, Date
from datetime import date


class Base(DeclarativeBase):
    pass


class WorkoutSet(Base):
    __tablename__ = "workout_sets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    exercise: Mapped[str] = mapped_column(String(100), nullable=False)
    weight: Mapped[float] = mapped_column(Numeric(6, 2), nullable=False)
    reps: Mapped[int] = mapped_column(Integer, nullable=False)
    workout_date: Mapped[date] = mapped_column(Date, nullable=False)
    set_number: Mapped[int] = mapped_column(Integer, nullable=False)
    