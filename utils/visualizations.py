import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st

def plot_entropy(p):
    """Plot binary entropy function."""
    fig, ax = plt.subplots()
    x = np.linspace(0.001, 0.999, 100)
    y = -x * np.log2(x) - (1-x) * np.log2(1-x)
    ax.plot(x, y)
    ax.set_xlabel('p')
    ax.set_ylabel('H(p)')
    ax.set_title('Binary Entropy Function')
    ax.grid(True)
    return fig

def plot_joint_distribution(joint_prob):
    """Plot joint probability distribution."""
    fig = go.Figure(data=[go.Heatmap(
        z=joint_prob,
        colorscale='Viridis')])
    fig.update_layout(
        title='Joint Probability Distribution',
        xaxis_title='X',
        yaxis_title='Y'
    )
    return fig

def plot_channel(p_error):
    """Plot binary symmetric channel."""
    fig = go.Figure()
    
    # Add nodes
    fig.add_trace(go.Scatter(
        x=[0, 1, 0, 1],
        y=[1, 1, 0, 0],
        mode='markers+text',
        text=['0', '1', '0', '1'],
        textposition="top center",
        name='Nodes'
    ))
    
    # Add arrows
    fig.add_annotation(
        x=0, y=1,
        ax=0, ay=0,
        xref='x', yref='y',
        axref='x', ayref='y',
        text=f'{1-p_error:.2f}',
        showarrow=True
    )
    
    fig.add_annotation(
        x=1, y=1,
        ax=1, ay=0,
        xref='x', yref='y',
        axref='x', ayref='y',
        text=f'{1-p_error:.2f}',
        showarrow=True
    )
    
    fig.update_layout(
        title='Binary Symmetric Channel',
        showlegend=False
    )
    
    return fig
