# Information Theory with Python

An interactive online book for learning information theory concepts with Python implementations. This project provides hands-on experience with fundamental concepts like Entropy, Mutual Information, and Channel Capacity through interactive examples and visualizations.

## Features

- **Interactive Learning**: Experiment with information theory concepts in real-time
- **Python Implementation**: Practical code examples for every concept
- **Downloadable Notebooks**: Jupyter notebooks for each chapter
- **No Login Required**: Open access educational content
- **Visual Understanding**: Interactive plots and visualizations

## Chapters

1. **Entropy and Information**
   - Shannon Entropy fundamentals and definitions
   - Interactive binary entropy function visualization
   - Practical entropy calculations with Python
   - Downloadable Jupyter notebooks with exercises
   - Real-world applications of entropy

2. **Mutual Information**
   - Understanding information dependency between variables
   - Interactive joint probability distribution explorer
   - Visualization of mutual information concepts
   - Practical implementation with NumPy
   - Case studies and exercises

3. **Channel Capacity**
   - Binary Symmetric Channel analysis and visualization
   - Interactive channel capacity calculator
   - Error probability impact on capacity
   - Python implementation of capacity calculations
   - Practical exercises and examples

## Project Structure

```
.
├── main.py                 # Main application entry point
├── pages/                  # Chapter content
│   ├── 01_entropy.py      # Entropy chapter
│   ├── 02_mutual_information.py
│   └── 03_channel_capacity.py
├── utils/                  # Utility functions
│   ├── examples.py        # Core calculations
│   ├── visualizations.py  # Plotting functions
│   └── notebook_generator.py
├── style.css              # Custom styling
└── .streamlit/            # Streamlit configuration
```

## Technologies Used

- **Streamlit**: Interactive web application framework
- **Matplotlib**: Static visualizations and plots
- **Plotly**: Interactive graphs and visualizations
- **NumPy**: Numerical computations and array operations
- **nbformat**: Jupyter notebook generation
- **Python 3.11**: Core programming language

## Getting Started

Visit our GitHub Pages site: https://shreyasfadnavis.github.io/InfoTheoryInPython/

Or run locally:

```bash
# Clone the repository
git clone https://github.com/ShreyasFadnavis/InfoTheoryInPython.git
cd InfoTheoryInPython

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run main.py
```

## Development Setup

1. **Prerequisites**:
   - Python 3.11 or higher
   - pip package manager

2. **Environment Setup**:
   ```bash
   # Install required packages
   pip install -r requirements.txt
   ```

3. **Running the Development Server**:
   ```bash
   # Start the Streamlit server
   streamlit run main.py
   ```

4. **Development Workflow**:
   - Make changes to the Python files
   - Streamlit will automatically reload on file changes
   - Test your changes in the browser
   - Run the notebook generation to update downloadable content

## Contributing Guidelines

1. **Fork and Clone**:
   - Fork the repository on GitHub
   - Clone your fork locally

2. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Development**:
   - Follow the project structure
   - Add tests for new functionality
   - Ensure code quality and documentation
   - Test locally before submitting

4. **Submit Changes**:
   - Commit your changes with clear messages
   - Push to your fork
   - Create a Pull Request with a clear description

5. **Code Style**:
   - Follow PEP 8 guidelines
   - Use meaningful variable names
   - Add docstrings for functions
   - Comment complex algorithms

## License

This project is open source and available under the MIT License.
