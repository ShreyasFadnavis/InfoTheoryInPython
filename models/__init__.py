from .base import Base, engine
from .user import User
from .progress import ChapterProgress, ExerciseAttempt

def init_db():
    from sqlalchemy import inspect
    inspector = inspect(engine)
    
    # Get all table names
    existing_tables = inspector.get_table_names()
    
    # Create tables that don't exist yet
    for table in Base.metadata.sorted_tables:
        if table.name not in existing_tables:
            table.create(bind=engine)
