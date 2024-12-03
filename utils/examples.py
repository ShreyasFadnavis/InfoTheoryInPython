import numpy as np

def calculate_entropy(p):
    """Calculate entropy of a binary random variable."""
    if p <= 0 or p >= 1:
        return 0
    return -p * np.log2(p) - (1-p) * np.log2(1-p)

def calculate_mutual_information(joint_prob):
    """Calculate mutual information from joint probability distribution."""
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

def calculate_channel_capacity(p_error):
    """Calculate capacity of binary symmetric channel."""
    return 1 + p_error * np.log2(p_error) + (1-p_error) * np.log2(1-p_error)
