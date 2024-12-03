import streamlit as st
import io
from utils.notebook_generator import generate_notebook_download
import numpy as np
from utils.visualizations import plot_entropy
from utils.examples import calculate_entropy

st.title("Chapter 1: Entropy and Information")

st.markdown("""
### Shannon Entropy

The fundamental measure of information in information theory is entropy. For a discrete random
variable X, the entropy H(X) measures the average amount of information contained in X.

For a binary random variable with probability p of one outcome:

$$
H(p) = -p\log_2(p) - (1-p)\log_2(1-p)
$$
""")

st.markdown("### Interactive Example: Binary Entropy")

# Interactive entropy calculation
p = st.slider("Select probability p:", 0.0, 1.0, 0.5, 0.01)
entropy = calculate_entropy(p)

st.markdown(f"""
The entropy for p = {p:.2f} is H(p) = {entropy:.4f} bits.

Try the following code:
""")

code = f"""
import numpy as np

def calculate_entropy(p):
    if p <= 0 or p >= 1:
        return 0
    return -p * np.log2(p) - (1-p) * np.log2(1-p)

# Calculate entropy for p = {p}
entropy = calculate_entropy({p})
print(f"Entropy: {{entropy:.4f}} bits")
"""

st.code(code, language='python')

# Plot entropy function
st.markdown("### Visualization of Binary Entropy Function")
fig = plot_entropy(p)
st.pyplot(fig)

st.markdown("""
### Properties of Entropy

1. **Non-negativity**: H(X) ≥ 0
2. **Maximum entropy**: For binary random variables, H(X) ≤ 1 bit
3. **Concavity**: The entropy function is concave

### Exercise

Try to:
1. Find the probability that gives maximum entropy
2. Calculate entropy for very small probabilities

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
3. Observe how entropy changes as probability approaches 0 or 1
""")
