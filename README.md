# Learning Machines: Companion Notebooks

Jupyter notebooks accompanying the textbook *Learning Machines: A Statistical Introduction*, by [Gregory Wheeler](https://gregorywheeler.org/).

The textbook cross-references each notebook by filename in a footnote at the opening of the corresponding chapter.

## Notebooks by Chapter

| Notebook | Chapter | Description |
|----------|---------|-------------|
| `ch01_01_baseline.ipynb` | 1 | The baseline model: why the mean minimizes squared error, and what one feature buys |
| `ch02_01_polynomial_regression.ipynb` | 2 | Polynomial regression and the bias-variance tradeoff |
| `ch02_02_linear_regression_ols.ipynb` | 2 | OLS closed-form solution and matrix formulation |
| `ch02_03_bayesian_regression.ipynb` | 2 | Bayesian linear regression with PyMC *(optional)* |
| `ch02_04_applied.ipynb` | 2 | Applied: OLS on California housing and auto-mpg datasets |
| `ch03_01_gradient_descent.ipynb` | 3 | Gradient descent visualization and variants |
| `ch04_01_logistic_regression.ipynb` | 4 | Logistic regression from scratch |
| `ch04_02_multiclass.ipynb` | 4 | Multi-class classification with softmax |
| `ch04_03_applied.ipynb` | 4 | Applied: logistic regression and LDA on the Pima diabetes data |
| `ch05_01_bias_variance.ipynb` | 5 | Bias-variance decomposition |
| `ch06_01_model_evaluation.ipynb` | 6 | Cross-validation, confusion matrices, ROC curves |
| `ch06_02_applied.ipynb` | 6 | Applied: putting a trained classifier through the evaluation kit |
| `ch07_01_regularization.ipynb` | 7 | Ridge, LASSO, and Elastic Net regularization |
| `ch07_02_applied.ipynb` | 7 | Applied: ridge and LASSO paths on a problem with a known sparse truth |
| `ch08_01_trees_ensembles.ipynb` | 8 | Decision trees, random forests, gradient boosting |
| `ch08_02_kernel_methods.ipynb` | 8 | Kernel trick and support vector machines |
| `ch08_03_applied.ipynb` | 8 | Applied: breast-cancer ensembles and decision boundaries across model classes |
| `ch09_01_backpropagation.ipynb` | 9 | Backpropagation algorithm visualization |
| `ch09_02_applied.ipynb` | 9 | Applied: a feed-forward classifier in PyTorch on Fashion-MNIST |
| `ch10_01_convnets.ipynb` | 10 | Convolutional neural networks with PyTorch |
| `ch10_02_applied.ipynb` | 10 | Applied: a convolutional network on Fashion-MNIST, same training loop |
| `ch11_01_attention_transformers.ipynb` | 11 | Attention mechanisms and transformers |
| `ch11_02_applied.ipynb` | 11 | Applied: a self-attention head and a transformer block from scratch |
| `ch12_01_build_a_gpt.ipynb` | 12 | **Capstone:** build and train a small GPT on a laptop |
| `ch13_01_unsupervised.ipynb` | 13 | Unsupervised Fashion-MNIST: PCA, K-means, and an autoencoder with the labels sealed |

## Dependencies

```bash
pip install -r requirements.txt
```

Core dependencies:
- **numpy** - Numerical computing
- **pandas** - Data manipulation
- **matplotlib** - Visualization
- **scipy** - Statistical functions (Chapter 2)
- **scikit-learn** - Machine learning (Chapters 2-8)
- **torch** - Deep learning (Chapters 9-11)
- **torchvision** - Image datasets and transforms (Chapter 10)

Optional dependencies:
- **pymc** - Bayesian inference (ch02_03 only)
- **arviz** - Bayesian visualization (ch02_03 only)

## Environment Setup

```bash
# Create a virtual environment (recommended)
python -m venv mlone_env
source mlone_env/bin/activate  # On Windows: mlone_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

## Notes

- Some notebooks download datasets on first run (e.g., MNIST for the ConvNets notebook, ~11MB)
- Notebooks are designed to be run sequentially within each chapter
- All figures use the `mlone_theme.py` styling module for visual consistency

## Contributing

Found an error? See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on submitting fixes.

## Related Resources

- Textbook: *Learning Machines: A Statistical Introduction*
