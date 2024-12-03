from models.base import SessionLocal
from models.progress import ChapterProgress, ExerciseAttempt
import streamlit as st
from datetime import datetime

def track_chapter_visit(chapter_id: str):
    if not st.session_state.user:
        return
    
    db = SessionLocal()
    try:
        progress = (
            db.query(ChapterProgress)
            .filter(
                ChapterProgress.user_id == st.session_state.user.id,
                ChapterProgress.chapter_id == chapter_id
            )
            .first()
        )
        
        if progress:
            progress.last_visited = datetime.now()
        else:
            progress = ChapterProgress(
                user_id=st.session_state.user.id,
                chapter_id=chapter_id
            )
            db.add(progress)
            
        db.commit()
    finally:
        db.close()

def mark_chapter_completed(chapter_id: str, score: float = None):
    if not st.session_state.user:
        return
    
    db = SessionLocal()
    try:
        progress = (
            db.query(ChapterProgress)
            .filter(
                ChapterProgress.user_id == st.session_state.user.id,
                ChapterProgress.chapter_id == chapter_id
            )
            .first()
        )
        
        if progress:
            progress.completed = True
            if score is not None:
                progress.score = score
        else:
            progress = ChapterProgress(
                user_id=st.session_state.user.id,
                chapter_id=chapter_id,
                completed=True,
                score=score if score is not None else 0.0
            )
            db.add(progress)
            
        db.commit()
    finally:
        db.close()

def track_exercise_attempt(chapter_id: str, exercise_id: str, completed: bool = False):
    if not st.session_state.user:
        return
    
    db = SessionLocal()
    try:
        attempt = (
            db.query(ExerciseAttempt)
            .filter(
                ExerciseAttempt.user_id == st.session_state.user.id,
                ExerciseAttempt.chapter_id == chapter_id,
                ExerciseAttempt.exercise_id == exercise_id
            )
            .first()
        )
        
        if attempt:
            attempt.attempt_count += 1
            attempt.completed = completed
            attempt.last_attempt = datetime.now()
        else:
            attempt = ExerciseAttempt(
                user_id=st.session_state.user.id,
                chapter_id=chapter_id,
                exercise_id=exercise_id,
                completed=completed
            )
            db.add(attempt)
            
        db.commit()
    finally:
        db.close()

def get_user_progress():
    if not st.session_state.user:
        return None
    
    db = SessionLocal()
    try:
        progress = (
            db.query(ChapterProgress)
            .filter(ChapterProgress.user_id == st.session_state.user.id)
            .all()
        )
        return progress
    finally:
        db.close()
