# Learning Machines: Companion Notebooks

Companion notebooks for the textbook *Learning Machines: A Statistical Introduction*,
by [Gregory Wheeler](https://gregorywheeler.org/).

> ### Nothing to install
>
> **[welr.github.io/learning-machines-site](https://welr.github.io/learning-machines-site/)**
>
> Every classical chapter runs in your browser — **Python and R side by side**, no
> download, no environment, no account. The deep-learning chapters open in Google
> Colab with one click. Start there; this repository is the source behind it.

The textbook cross-references each notebook by filename in a footnote at the opening
of the corresponding chapter.

## Three ways to run these

**1. In your browser — recommended.** The [companion
site](https://welr.github.io/learning-machines-site/) runs 18 of these notebooks live
on the page, each one in both Python and R, using Pyodide and WebR. Nothing is
installed and nothing is sent anywhere: the code executes on your own machine, inside
the tab.

**2. In Colab — for the PyTorch chapters.** Anything needing a GPU or a large
download links out to Colab. Every notebook here is self-contained, so a Colab click
just works: the plotting theme is fetched at run time, and datasets download on first
use. Free Google account required.

**3. Locally — if you want to modify and keep things.** Clone the repository and
install the dependencies below. This is the only route that needs a Python
environment, and the only reason to prefer it is that your changes persist.

## Notebooks

| Ch | Notebook | What it does | Run it |
|----|----------|--------------|--------|
| **1** | [`ch01_01_baseline.ipynb`](ch01_01_baseline.ipynb) | The baseline model: why the mean minimizes squared error, and what one feature buys | [Colab](https://colab.research.google.com/github/welr/learning_machines/blob/main/ch01_01_baseline.ipynb) |
| **2** | [`ch02_01_polynomial_regression.ipynb`](ch02_01_polynomial_regression.ipynb) | Polynomial regression and the bias-variance tradeoff | [browser](https://welr.github.io/learning-machines-site/chapters/ch02_01_polynomial_regression.html) |
| **2** | [`ch02_02_linear_regression_ols.ipynb`](ch02_02_linear_regression_ols.ipynb) | OLS closed-form solution and matrix formulation | [browser](https://welr.github.io/learning-machines-site/chapters/ch02_02_linear_regression_ols.html) |
| **2** | [`ch02_03_bayesian_regression.ipynb`](ch02_03_bayesian_regression.ipynb) | Bayesian linear regression with PyMC *(optional)* | [browser](https://welr.github.io/learning-machines-site/chapters/ch02_03_bayesian_regression.html) · [Colab](https://colab.research.google.com/github/welr/learning_machines/blob/main/ch02_03_bayesian_regression.ipynb) |
| **2** | [`ch02_04_applied.ipynb`](ch02_04_applied.ipynb) | Applied: OLS on California housing and auto-mpg datasets | [browser](https://welr.github.io/learning-machines-site/chapters/ch02_04_applied.html) |
| **3** | [`ch03_01_gradient_descent.ipynb`](ch03_01_gradient_descent.ipynb) | Gradient descent visualization and variants | [browser](https://welr.github.io/learning-machines-site/chapters/ch03_01_gradient_descent.html) |
| **4** | [`ch04_01_logistic_regression.ipynb`](ch04_01_logistic_regression.ipynb) | Logistic regression from scratch | [browser](https://welr.github.io/learning-machines-site/chapters/ch04_01_logistic_regression.html) |
| **4** | [`ch04_02_multiclass.ipynb`](ch04_02_multiclass.ipynb) | Multi-class classification with softmax | [browser](https://welr.github.io/learning-machines-site/chapters/ch04_02_multiclass.html) |
| **4** | [`ch04_03_applied.ipynb`](ch04_03_applied.ipynb) | Applied: logistic regression and LDA on the Pima diabetes data | [browser](https://welr.github.io/learning-machines-site/chapters/ch04_03_applied.html) |
| **5** | [`ch05_01_bias_variance.ipynb`](ch05_01_bias_variance.ipynb) | Bias-variance decomposition | [browser](https://welr.github.io/learning-machines-site/chapters/ch05_01_bias_variance.html) |
| **6** | [`ch06_01_model_evaluation.ipynb`](ch06_01_model_evaluation.ipynb) | Cross-validation, confusion matrices, ROC curves | [browser](https://welr.github.io/learning-machines-site/chapters/ch06_01_model_evaluation.html) |
| **6** | [`ch06_02_applied.ipynb`](ch06_02_applied.ipynb) | Applied: putting a trained classifier through the evaluation kit | [browser](https://welr.github.io/learning-machines-site/chapters/ch06_02_applied.html) |
| **7** | [`ch07_01_regularization.ipynb`](ch07_01_regularization.ipynb) | Ridge, LASSO, and Elastic Net regularization | [browser](https://welr.github.io/learning-machines-site/chapters/ch07_01_regularization.html) |
| **7** | [`ch07_02_applied.ipynb`](ch07_02_applied.ipynb) | Applied: ridge and LASSO paths on a problem with a known sparse truth | [browser](https://welr.github.io/learning-machines-site/chapters/ch07_02_applied.html) |
| **8** | [`ch08_01_trees_ensembles.ipynb`](ch08_01_trees_ensembles.ipynb) | Decision trees, random forests, gradient boosting | [browser](https://welr.github.io/learning-machines-site/chapters/ch08_01_trees_ensembles.html) |
| **8** | [`ch08_02_kernel_methods.ipynb`](ch08_02_kernel_methods.ipynb) | Kernel trick and support vector machines | [browser](https://welr.github.io/learning-machines-site/chapters/ch08_02_kernel_methods.html) |
| **8** | [`ch08_03_applied.ipynb`](ch08_03_applied.ipynb) | Applied: breast-cancer ensembles and decision boundaries across model classes | [browser](https://welr.github.io/learning-machines-site/chapters/ch08_03_applied.html) |
| **9** | [`ch09_01_backpropagation.ipynb`](ch09_01_backpropagation.ipynb) | Backpropagation algorithm visualization | [browser](https://welr.github.io/learning-machines-site/chapters/ch09_01_backpropagation.html) |
| **9** | [`ch09_02_applied.ipynb`](ch09_02_applied.ipynb) | Applied: a feed-forward classifier in PyTorch on Fashion-MNIST | [Colab](https://colab.research.google.com/github/welr/learning_machines/blob/main/ch09_02_applied.ipynb) |
| **10** | [`ch10_01_convnets.ipynb`](ch10_01_convnets.ipynb) | Convolutional neural networks with PyTorch | [Colab](https://colab.research.google.com/github/welr/learning_machines/blob/main/ch10_01_convnets.ipynb) |
| **10** | [`ch10_02_applied.ipynb`](ch10_02_applied.ipynb) | Applied: a convolutional network on Fashion-MNIST, same training loop | [Colab](https://colab.research.google.com/github/welr/learning_machines/blob/main/ch10_02_applied.ipynb) |
| **11** | [`ch11_01_attention_transformers.ipynb`](ch11_01_attention_transformers.ipynb) | Attention mechanisms and transformers | [Colab](https://colab.research.google.com/github/welr/learning_machines/blob/main/ch11_01_attention_transformers.ipynb) |
| **11** | [`ch11_02_applied.ipynb`](ch11_02_applied.ipynb) | Applied: a self-attention head and a transformer block from scratch | [Colab](https://colab.research.google.com/github/welr/learning_machines/blob/main/ch11_02_applied.ipynb) |
| **12** | [`ch12_01_build_a_gpt.ipynb`](ch12_01_build_a_gpt.ipynb) | **Capstone:** build and train a small GPT on a laptop | [Colab](https://colab.research.google.com/github/welr/learning_machines/blob/main/ch12_01_build_a_gpt.ipynb) |
| **13** | [`ch13_01_unsupervised.ipynb`](ch13_01_unsupervised.ipynb) | Unsupervised Fashion-MNIST: PCA, K-means, and an autoencoder with the labels sealed | [browser](https://welr.github.io/learning-machines-site/chapters/ch13_01_unsupervised.html) · [Colab](https://colab.research.google.com/github/welr/learning_machines/blob/main/ch13_01_unsupervised.ipynb) |

Chapter 1's material is on the site's [landing
page](https://welr.github.io/learning-machines-site/) rather than a chapter page of
its own.

## Running locally

Only needed for route 3 above.

```bash
git clone https://github.com/welr/learning_machines.git
cd learning_machines

python -m venv mlone_env
source mlone_env/bin/activate      # Windows: mlone_env\Scripts\activate
pip install -r requirements.txt

jupyter notebook
```

**Dependencies.** numpy, pandas, matplotlib (plotting and numerics); scipy
(statistical functions, Chapter 2); scikit-learn (Chapters 2–8); torch and
torchvision (Chapters 9–12). For the optional Bayesian notebook `ch02_03`, also
`pip install pymc arviz` — it is not in `requirements.txt`, and the notebook
degrades gracefully if they are missing.

**Notes.**

- Some notebooks download data on first run: MNIST and Fashion-MNIST (~11–30 MB),
  and about a megabyte of Shakespeare for the GPT capstone.
- Notebooks within a chapter are meant to be read in order.
- All figures use `mlone_theme.py` for visual consistency with the book.

## Licence

MIT — see [LICENSE](LICENSE). Third-party code and data, with the notices their
licences require, are recorded in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Contributing

Found an error? See [CONTRIBUTING.md](CONTRIBUTING.md).
