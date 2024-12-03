import streamlit as st
import io
from utils.notebook_generator import generate_notebook_download
import numpy as np
from utils.visualizations import plot_entropy
from utils.examples import calculate_entropy


st.title("Chapter 1: Entropy and Information")

st.markdown("""
### Introduction to Entropy

In information theory, entropy is a measure of the average amount of information contained in a message.
The concept was introduced by Claude Shannon in his seminal 1948 paper "A Mathematical Theory of Communication".

#### Mathematical Definition

For a discrete random variable X with possible values {x₁, ..., xₙ} and probability mass function P(X),
the entropy H(X) is defined as:

H(X) = -∑P(x)log₂P(x)

For a binary random variable (with probability p and 1-p), this simplifies to:

H(p) = -p log₂(p) - (1-p)log₂(1-p)
""")

# Interactive Example
st.markdown("### Interactive Example: Binary Entropy Function")

# Slider for probability
p = st.slider("Select probability p:", 0.0, 1.0, 0.5, 0.01)

# Calculate and display entropy
entropy = calculate_entropy(p)
st.write(f"Entropy H(p) = {entropy:.3f} bits")

# Plot entropy function
st.pyplot(plot_entropy(p))

# Code example
st.markdown("### Python Implementation")
st.markdown("""
Here's how to calculate the entropy of a binary random variable:
""")

code = """
import numpy as np

def calculate_entropy(p):
    if p <= 0 or p >= 1:
        return 0
    return -p * np.log2(p) - (1-p) * np.log2(1-p)

# Example usage
p = 0.5
entropy = calculate_entropy(p)
print(f"Entropy for p={p}: {entropy:.3f} bits")
"""

st.code(code, language="python")

st.markdown("""
### Exercises

Try to:
1. Find the probability that gives maximum entropy
2. Calculate entropy for very small probabilities
3. Observe how entropy changes as probability approaches 0 or 1
""")

# Add download button for notebook
with open(__file__, 'r') as f:
    chapter_content = f.read()

notebook_content = generate_notebook_download(chapter_content, "Information Theory: Entropy")
notebook_bytes = notebook_content.encode()

st.download_button(
    label="Download as Jupyter Notebook",
    data=notebook_bytes,
    file_name="entropy_chapter.ipynb",
    mime="application/x-ipynb+json"
)
