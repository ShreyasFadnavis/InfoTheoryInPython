import streamlit as st
import numpy as np
from utils.visualizations import plot_joint_distribution
from utils.examples import calculate_mutual_information

st.title("Chapter 2: Mutual Information")

st.markdown("""
### Mutual Information

Mutual Information (MI) measures the mutual dependence between two variables. It quantifies the
amount of information obtained about one random variable by observing another random variable.

For random variables X and Y:

$$
I(X;Y) = \sum_{x,y} p(x,y) \log_2 \\frac{p(x,y)}{p(x)p(y)}
$$
""")

st.markdown("### Interactive Example: Mutual Information")

# Create interactive joint probability matrix
st.markdown("Adjust the joint probability distribution:")
col1, col2 = st.columns(2)

with col1:
    p00 = st.slider("P(X=0,Y=0):", 0.0, 1.0, 0.25, 0.01)
    p01 = st.slider("P(X=0,Y=1):", 0.0, 1.0, 0.25, 0.01)

with col2:
    p10 = st.slider("P(X=1,Y=0):", 0.0, 1.0, 0.25, 0.01)
    p11 = st.slider("P(X=1,Y=1):", 0.0, 1.0, 0.25, 0.01)

# Normalize probabilities
total = p00 + p01 + p10 + p11
joint_prob = np.array([[p00/total, p01/total], 
                      [p10/total, p11/total]])

mi = calculate_mutual_information(joint_prob)

st.markdown(f"""
The mutual information for this joint distribution is: {mi:.4f} bits

Try the following code:
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
"""

st.code(code, language='python')

# Visualize joint distribution
st.markdown("### Visualization of Joint Distribution")
fig = plot_joint_distribution(joint_prob)
st.plotly_chart(fig)

st.markdown("""
### Properties of Mutual Information

1. **Non-negativity**: I(X;Y) ≥ 0
2. **Symmetry**: I(X;Y) = I(Y;X)
3. **Relationship with entropy**: I(X;Y) = H(X) - H(X|Y)

### Exercise

Try to:
1. Create independent variables (MI should be 0)
2. Create perfectly correlated variables (maximum MI)
3. Observe how MI changes with different probability distributions
""")
