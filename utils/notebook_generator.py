import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
import re

def extract_markdown_and_code(content):
    """Extract markdown and code blocks from the chapter content."""
    # Remove streamlit-specific imports and commands
    content = re.sub(r'import streamlit as st\n', '', content)
    content = re.sub(r'st\.[a-zA-Z_]+\((.*?)\)\n?', '', content)
    
    sections = []
    lines = content.split('\n')
    current_block = []
    current_type = None
    
    for line in lines:
        if line.strip().startswith('"""') or line.strip().startswith("'''"):
            if current_type == 'markdown':
                # End markdown block
                if current_block:
                    sections.append(('markdown', '\n'.join(current_block)))
                current_block = []
                current_type = None
            else:
                # Start markdown block
                current_type = 'markdown'
            continue
            
        if line.strip().startswith('code = """') or line.strip().startswith("code = '''"):
            if current_block:
                sections.append(('markdown' if current_type == 'markdown' else 'code', 
                               '\n'.join(current_block)))
            current_block = []
            current_type = 'code_example'
            continue
            
        if current_type == 'markdown' and line.strip():
            current_block.append(line)
        elif line.strip() and not line.strip().startswith('st.'):
            if current_type != 'code_example':
                if current_block:
                    sections.append(('markdown' if current_type == 'markdown' else 'code',
                                   '\n'.join(current_block)))
                current_block = []
            current_block.append(line)
            current_type = 'code'
    
    if current_block:
        sections.append(('markdown' if current_type == 'markdown' else 'code',
                        '\n'.join(current_block)))
    
    return sections

def create_notebook(chapter_content, title):
    """Create a Jupyter notebook from chapter content."""
    nb = new_notebook()
    
    # Add title
    nb.cells.append(new_markdown_cell(f"# {title}"))
    
    # Process content
    sections = extract_markdown_and_code(chapter_content)
    
    for section_type, content in sections:
        if content.strip():  # Only add non-empty cells
            if section_type == 'markdown':
                nb.cells.append(new_markdown_cell(content))
            else:
                nb.cells.append(new_code_cell(content))
    
    return nb

def generate_notebook_download(chapter_content, title):
    """Generate a notebook and return it as a string."""
    nb = create_notebook(chapter_content, title)
    return nbformat.writes(nb)
