import streamlit as st
import base64

st.set_page_config(
    page_title="Information Theory with Python",
    page_icon="📚",
    layout="wide"
)

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
