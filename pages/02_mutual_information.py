import streamlit as st
import io
from utils.notebook_generator import generate_notebook_download
import numpy as np
from utils.visualizations import plot_joint_distribution
from utils.examples import calculate_mutual_information

st.title("Chapter 2: Mutual Information")

st.markdown("""
### Introduction to Mutual Information

Mutual Information (MI) measures the mutual dependence between two variables.
It quantifies the amount of information obtained about one random variable by observing another random variable.

#### Mathematical Definition

For two random variables X and Y, the mutual information I(X;Y) is defined as:

I(X;Y) = ∑∑P(x,y)log₂(P(x,y)/(P(x)P(y)))

where P(x,y) is the joint probability distribution, and P(x) and P(y) are the marginal distributions.
""")

# Interactive Example
st.markdown("### Interactive Example: Joint Distribution")

# Create a 2x2 joint distribution matrix
st.markdown("Adjust the joint probability distribution:")
p00 = st.slider("P(X=0,Y=0):", 0.0, 1.0, 0.25, 0.01)
p01 = st.slider("P(X=0,Y=1):", 0.0, 1.0-p00, 0.25, 0.01)
p10 = st.slider("P(X=1,Y=0):", 0.0, 1.0-p00-p01, 0.25, 0.01)
p11 = 1.0 - p00 - p01 - p10

joint_prob = np.array([[p00, p01], [p10, p11]])

# Display the distribution
st.plotly_chart(plot_joint_distribution(joint_prob))

# Calculate and display MI
mi = calculate_mutual_information(joint_prob)
st.write(f"Mutual Information I(X;Y) = {mi:.3f} bits")

# Code example
st.markdown("### Python Implementation")
st.markdown("""
Here's how to calculate mutual information from a joint probability distribution:
""")

code = """
import numpy as np

def calculate_mutual_information(joint_prob):
    # Marginal probabilities
    p_x = np.sum(joint_prob, axis=1)
    p_y = np.sum(joint_prob, axis=0)
    
    # Calculate mutual information
    mi = 0
    for i in range(len(p_x)):
        for j in range(len(p_y)):
            if joint_prob[i,j] > 0:
                mi += joint_prob[i,j] * np.log2(joint_prob[i,j] / (p_x[i] * p_y[j]))
    return mi

# Example usage
joint_prob = np.array([[0.25, 0.25], [0.25, 0.25]])
mi = calculate_mutual_information(joint_prob)
print(f"Mutual Information: {mi:.3f} bits")
"""

st.code(code, language="python")

st.markdown("""
### Exercises

Try to:
1. Create independent variables (MI should be 0)
2. Create perfectly correlated variables (maximum MI)
3. Observe how MI changes with different probability distributions
""")

# Add download button for notebook
with open(__file__, 'r') as f:
    chapter_content = f.read()

notebook_content = generate_notebook_download(chapter_content, "Information Theory: Mutual Information")
notebook_bytes = notebook_content.encode()

st.download_button(
    label="Download as Jupyter Notebook",
    data=notebook_bytes,
    file_name="mutual_information_chapter.ipynb",
    mime="application/x-ipynb+json"
)
