import streamlit as st
import io
from utils.notebook_generator import generate_notebook_download
import numpy as np
from utils.visualizations import plot_channel
from utils.examples import calculate_channel_capacity

st.title("Chapter 3: Channel Capacity")

st.markdown("""
### Introduction to Channel Capacity

Channel capacity is the maximum rate at which information can be reliably transmitted over a communication channel.
We'll focus on the binary symmetric channel (BSC) as a simple example.

#### Mathematical Definition

For a binary symmetric channel with error probability p, the capacity C is:

C = 1 + p log₂(p) + (1-p)log₂(1-p)

where p is the probability of bit flip (error) during transmission.
""")

# Interactive Example
st.markdown("### Interactive Example: Binary Symmetric Channel")

# Slider for error probability
p_error = st.slider("Select error probability:", 0.0, 0.5, 0.1, 0.01)

# Display channel diagram
st.plotly_chart(plot_channel(p_error))

# Calculate and display capacity
capacity = calculate_channel_capacity(p_error)
st.write(f"Channel Capacity = {capacity:.3f} bits/transmission")

# Code example
st.markdown("### Python Implementation")
st.markdown("""
Here's how to calculate the capacity of a binary symmetric channel:
""")

code = """
import numpy as np

def calculate_channel_capacity(p_error):
    return 1 + p_error * np.log2(p_error) + (1-p_error) * np.log2(1-p_error)

# Example usage
p_error = 0.1
capacity = calculate_channel_capacity(p_error)
print(f"Channel Capacity: {capacity:.3f} bits/transmission")
"""

st.code(code, language="python")

st.markdown("""
### Exercises

Try to:
1. Find the capacity when p_error = 0.5
2. Calculate capacity for very small error probabilities
3. Observe how capacity changes with different error probabilities
""")

# Add download button for notebook
with open(__file__, 'r') as f:
    chapter_content = f.read()

notebook_content = generate_notebook_download(chapter_content, "Information Theory: Channel Capacity")
notebook_bytes = notebook_content.encode()

st.download_button(
    label="Download as Jupyter Notebook",
    data=notebook_bytes,
    file_name="channel_capacity_chapter.ipynb",
    mime="application/x-ipynb+json"
)
