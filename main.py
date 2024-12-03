import streamlit as st
import base64
from auth import init_session_state, login_user, logout_user, register_user
from models import init_db
from progress_tracker import get_user_progress

# Initialize the database
init_db()

st.set_page_config(
    page_title="Information Theory with Python",
    page_icon="📚",
    layout="wide"
)

# Initialize session state
init_session_state()

# Authentication UI in sidebar
with st.sidebar:
    if st.session_state.user:
        st.write(f"Welcome, {st.session_state.user.email}!")
        if st.button("Logout"):
            logout_user()
        
        # Display progress
        st.write("### Your Progress")
        progress = get_user_progress()
        if progress:
            for chapter in progress:
                status = "✅" if chapter.completed else "🔄"
                st.write(f"{status} {chapter.chapter_id}: {chapter.score:.1f}%")
    else:
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")
            if st.button("Login"):
                if login_user(email, password):
                    st.success("Logged in successfully!")
                    st.rerun()
                else:
                    st.error("Invalid credentials")
        
        with tab2:
            email = st.text_input("Email", key="register_email")
            password = st.text_input("Password", type="password", key="register_password")
            if st.button("Register"):
                if register_user(email, password):
                    st.success("Registration successful! Please login.")
                else:
                    st.error("Email already registered")

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("Information Theory with Python")
st.markdown("""
Welcome to this interactive book on Information Theory! This resource combines theoretical concepts
with practical Python implementations to help you understand the fundamentals of information theory.

### Contents

1. **Entropy and Information**
   - Shannon Entropy
   - Joint and Conditional Entropy
   - Interactive examples with probability distributions

2. **Mutual Information**
   - Definition and Properties
   - Relationship with Entropy
   - Practical applications

3. **Channel Capacity**
   - Binary Symmetric Channel
   - Channel Coding
   - Capacity calculations

### How to Use This Book

- Navigate through chapters using the sidebar
- Run interactive code examples
- Experiment with parameters
- Visualize results in real-time

Let's begin our journey into Information Theory! Select a topic from the sidebar to start learning.
""")

st.markdown("---")

st.markdown("""
### About This Book

This interactive book is designed to help students and practitioners understand information theory
concepts through hands-on Python implementations. Each chapter includes:

- 📖 Theoretical explanations
- 🔢 Mathematical formulations
- 💻 Interactive code examples
- 📊 Visualizations
- 🧪 Practical exercises
""")
