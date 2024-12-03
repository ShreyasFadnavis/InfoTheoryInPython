import streamlit as st
from models.base import SessionLocal
from models.user import User
import hashlib
import os
import secrets

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hash_password(plain_password) == hashed_password

def init_session_state():
    if 'user' not in st.session_state:
        st.session_state.user = None

def login_user(email: str, password: str) -> bool:
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user and verify_password(password, user.hashed_password):
            st.session_state.user = user
            return True
        return False
    finally:
        db.close()

def logout_user():
    st.session_state.user = None

def register_user(email: str, password: str) -> bool:
    db = SessionLocal()
    try:
        if db.query(User).filter(User.email == email).first():
            return False
        
        user = User(
            email=email,
            hashed_password=hash_password(password)
        )
        db.add(user)
        db.commit()
        return True
    finally:
        db.close()

def require_auth():
    if not st.session_state.user:
        st.warning("Please log in to access this feature")
        return False
    return True
