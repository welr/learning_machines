"""
Insert banners into all Learning Machines notebooks.
Generates base64-encoded images and inserts them as the first markdown cell.
"""

import json
from pathlib import Path
import create_banner

# Notebook -> Banner subtitle mapping
NOTEBOOKS = {
    "ch02_01_polynomial_regression.ipynb": "Polynomial Regression",
    "ch02_02_linear_regression_ols.ipynb": "Linear Regression: OLS",
    "ch03_01_gradient_descent.ipynb": "Gradient Descent",
    "ch04_01_logistic_regression.ipynb": "Logistic Regression",
    "ch04_02_multiclass.ipynb": "Multi-Class Classification",
    "ch05_01_bias_variance.ipynb": "Bias-Variance Tradeoff",
    "ch06_01_model_evaluation.ipynb": "Model Evaluation",
    "ch07_01_regularization.ipynb": "Regularization",
    "ch08_01_trees_ensembles.ipynb": "Trees and Ensembles",
    "ch09_01_backpropagation.ipynb": "Backpropagation",
    "ch10_01_convnets.ipynb": "Convolutional Networks",
    "ch11_01_attention_transformers.ipynb": "Attention and Transformers",
}

def insert_banner(notebook_path, subtitle):
    """Insert banner as first cell in notebook."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Generate the banner markdown
    banner_md = create_banner.generate_markdown_header(subtitle)

    # Create the banner cell
    banner_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [banner_md]
    }

    # Check if first cell is already a banner (contains our base64 image)
    if nb['cells'] and 'data:image/png;base64' in ''.join(nb['cells'][0].get('source', [])):
        # Replace existing banner
        nb['cells'][0] = banner_cell
        print(f"  Updated existing banner: {notebook_path.name}")
    else:
        # Insert new banner at top
        nb['cells'].insert(0, banner_cell)
        print(f"  Inserted new banner: {notebook_path.name}")

    # Write back
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

def main():
    notebooks_dir = Path(__file__).parent

    print("Inserting banners into notebooks...\n")

    for filename, subtitle in NOTEBOOKS.items():
        notebook_path = notebooks_dir / filename
        if notebook_path.exists():
            insert_banner(notebook_path, subtitle)
        else:
            print(f"  NOT FOUND: {filename}")

    print("\nDone!")

if __name__ == "__main__":
    main()
