from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from .base import Base

class ChapterProgress(Base):
    __tablename__ = "chapter_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    chapter_id = Column(String)  # e.g., "01_entropy"
    completed = Column(Boolean, default=False)
    last_visited = Column(DateTime(timezone=True), server_default=func.now())
    score = Column(Float, default=0.0)  # For tracking exercise performance

class ExerciseAttempt(Base):
    __tablename__ = "exercise_attempts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    chapter_id = Column(String)
    exercise_id = Column(String)
    attempt_count = Column(Integer, default=1)
    completed = Column(Boolean, default=False)
    last_attempt = Column(DateTime(timezone=True), server_default=func.now())
