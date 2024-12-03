import streamlit as st
import numpy as np
from utils.visualizations import plot_channel
from utils.examples import calculate_channel_capacity

st.title("Chapter 3: Channel Capacity")

st.markdown("""
### Channel Capacity

Channel capacity is the maximum rate at which information can be reliably transmitted over a
communication channel. For a binary symmetric channel (BSC), the capacity is:

$$
C = 1 - H(p)
$$

where p is the probability of error, and H(p) is the binary entropy function.
""")

st.markdown("### Interactive Example: Binary Symmetric Channel")

# Interactive channel capacity calculation
p_error = st.slider("Select error probability:", 0.0, 0.5, 0.1, 0.01)
capacity = calculate_channel_capacity(p_error)

st.markdown(f"""
The channel capacity for error probability p = {p_error:.2f} is C = {capacity:.4f} bits.

Try the following code:
""")

code = f"""
import numpy as np

def calculate_channel_capacity(p_error):
    return 1 + p_error * np.log2(p_error) + (1-p_error) * np.log2(1-p_error)

# Calculate capacity for p_error = {p_error}
capacity = calculate_channel_capacity({p_error})
print(f"Channel Capacity: {{capacity:.4f}} bits")
"""

st.code(code, language='python')

# Visualize channel
st.markdown("### Visualization of Binary Symmetric Channel")
fig = plot_channel(p_error)
st.plotly_chart(fig)

st.markdown("""
### Properties of Channel Capacity

1. **Maximum at p=0**: Capacity is maximum (1 bit) when there are no errors
2. **Minimum at p=0.5**: Capacity is 0 when the channel is completely random
3. **Symmetry**: C(p) = C(1-p)

### Exercise

Try to:
1. Find the capacity when p_error = 0.5
2. Calculate capacity for very small error probabilities
3. Observe how capacity changes with different error probabilities
""")
