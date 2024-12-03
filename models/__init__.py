from .base import Base, engine
from .user import User
from .progress import ChapterProgress, ExerciseAttempt

def init_db():
    Base.metadata.create_all(bind=engine)
