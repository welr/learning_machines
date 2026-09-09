# Learning Machines — notebook sources

Source notebooks behind the interactive companion to *Learning Machines: A
Statistical Introduction*, by [Gregory Wheeler](https://gregorywheeler.org/).

> ### Readers should start at the site
>
> **[welr.github.io/learning-machines-site](https://welr.github.io/learning-machines-site/)**
>
> That is where the book's code is published. Twenty-three of the twenty-seven pages run
> in your browser, in Python and R side by side, with nothing to install. The four
> that only train neural networks need PyTorch and open in Google Colab instead;
> seven more pages carry a Colab link beside their live cells.
>
> **You do not need this repository to use the book.** It holds the notebook sources
> the site is built from.

## If you arrived here from an "Open in Colab" button

You are in the right place — Colab opens these files directly, and everything needed
comes down at run time. Nothing to clone, nothing to install. Eleven notebooks are
reachable that way: the PyTorch chapters, the optional Bayesian notebook, and the
unsupervised coda.

## Map

Every notebook has a page on the site. The page is what the book cites; the notebook
is the source it was built from and, for the PyTorch chapters, the thing Colab runs.

| Ch | Page on the site | Runs | Source notebook here |
|----|------------------|------|----------------------|
| **1** | [The Baseline](https://welr.github.io/learning-machines-site/chapters/ch01_01_baseline.html) | browser | `ch01_01_baseline.ipynb` |
| **2** | [Polynomial Regression](https://welr.github.io/learning-machines-site/chapters/ch02_01_polynomial_regression.html) | browser | `ch02_01_polynomial_regression.ipynb` |
| **2** | [Ordinary Least Squares](https://welr.github.io/learning-machines-site/chapters/ch02_02_linear_regression_ols.html) | browser | `ch02_02_linear_regression_ols.ipynb` |
| **2** | [Bayesian Regression](https://welr.github.io/learning-machines-site/chapters/ch02_03_bayesian_regression.html) | browser | `ch02_03_bayesian_regression.ipynb` |
| **2** | [Applied — Regression in Practice](https://welr.github.io/learning-machines-site/chapters/ch02_04_applied.html) | browser | `ch02_04_applied.ipynb` |
| **3** | [Gradient Descent](https://welr.github.io/learning-machines-site/chapters/ch03_01_gradient_descent.html) | browser | `ch03_01_gradient_descent.ipynb` |
| **4** | [Logistic Regression](https://welr.github.io/learning-machines-site/chapters/ch04_01_logistic_regression.html) | browser | `ch04_01_logistic_regression.ipynb` |
| **4** | [Multi-Class Classification](https://welr.github.io/learning-machines-site/chapters/ch04_02_multiclass.html) | browser | `ch04_02_multiclass.ipynb` |
| **4** | [Applied — Logistic Regression, Odds, and a Generative Cousin](https://welr.github.io/learning-machines-site/chapters/ch04_03_applied.html) | browser | `ch04_03_applied.ipynb` |
| **5** | [The Bias–Variance Trade-off](https://welr.github.io/learning-machines-site/chapters/ch05_01_bias_variance.html) | browser | `ch05_01_bias_variance.ipynb` |
| **6** | [Model Evaluation](https://welr.github.io/learning-machines-site/chapters/ch06_01_model_evaluation.html) | browser | `ch06_01_model_evaluation.ipynb` |
| **6** | [Applied — Evaluating a Classifier](https://welr.github.io/learning-machines-site/chapters/ch06_02_applied.html) | browser | `ch06_02_applied.ipynb` |
| **7** | [Ridge and LASSO](https://welr.github.io/learning-machines-site/chapters/ch07_01_regularization.html) | browser | `ch07_01_regularization.ipynb` |
| **7** | [Applied — Ridge, LASSO, and the Regularization Path](https://welr.github.io/learning-machines-site/chapters/ch07_02_applied.html) | browser | `ch07_02_applied.ipynb` |
| **8** | [Decision Trees and Ensembles](https://welr.github.io/learning-machines-site/chapters/ch08_01_trees_ensembles.html) | browser | `ch08_01_trees_ensembles.ipynb` |
| **8** | [Kernel Methods](https://welr.github.io/learning-machines-site/chapters/ch08_02_kernel_methods.html) | browser | `ch08_02_kernel_methods.ipynb` |
| **8** | [Applied — Trees, Ensembles, and Decision Boundaries](https://welr.github.io/learning-machines-site/chapters/ch08_03_applied.html) | browser | `ch08_03_applied.ipynb` |
| **9** | [Backpropagation](https://welr.github.io/learning-machines-site/chapters/ch09_01_backpropagation.html) | browser | `ch09_01_backpropagation.ipynb` |
| **9** | [Applied — A Neural Network in PyTorch](https://welr.github.io/learning-machines-site/chapters/ch09_02_applied.html) | Colab | `ch09_02_applied.ipynb` |
| **10** | [Convolutional Networks](https://welr.github.io/learning-machines-site/chapters/ch10_01_convnets.html) | browser + Colab | `ch10_01_convnets.ipynb` |
| **10** | [Applied — A Convolutional Network](https://welr.github.io/learning-machines-site/chapters/ch10_02_applied.html) | Colab | `ch10_02_applied.ipynb` |
| **11** | [Attention and Transformers](https://welr.github.io/learning-machines-site/chapters/ch11_01_attention_transformers.html) | browser + Colab | `ch11_01_attention_transformers.ipynb` |
| **11** | [Applied — Attention from Scratch](https://welr.github.io/learning-machines-site/chapters/ch11_02_applied.html) | Colab | `ch11_02_applied.ipynb` |
| **12** | [Capstone — Build a GPT](https://welr.github.io/learning-machines-site/chapters/ch12_01_build_a_gpt.html) | browser + Colab | `ch12_01_build_a_gpt.ipynb` |
| **13** | [Structure Without Labels](https://welr.github.io/learning-machines-site/chapters/ch13_01_unsupervised.html) | browser | — |
| **13** | [Applied — Unsupervised Fashion-MNIST](https://welr.github.io/learning-machines-site/chapters/ch13_02_applied.html) | Colab | `ch13_02_applied.ipynb` |
| **13** | [Latent Semantic Analysis](https://welr.github.io/learning-machines-site/chapters/ch13_03_lsa.html) | browser + Colab | `ch13_03_lsa.ipynb` |

## Working on the notebooks

Only needed if you are modifying them. Readers do not need this.

```bash
git clone https://github.com/welr/learning_machines.git
cd learning_machines

python -m venv mlone_env
source mlone_env/bin/activate      # Windows: mlone_env\Scripts\activate
pip install -r requirements.txt

jupyter notebook
```

**Dependencies.** numpy, pandas, matplotlib, scipy, scikit-learn, torch,
torchvision. For the optional Bayesian notebook `ch02_03`, also
`pip install pymc arviz` — these are deliberately not in `requirements.txt`, and the
notebook degrades gracefully without them.

**Notes.**

- Some notebooks download data on first run: MNIST and Fashion-MNIST (~11–30 MB), and
  about a megabyte of Shakespeare for the GPT capstone.
- All figures use `mlone_theme.py`, which is also the canonical copy used by the
  book's figure scripts. Edit it here, not elsewhere.
- Notebooks are self-contained for Colab: `mlone_theme.py` is fetched at run time if
  it is not sitting beside the notebook.

**Keeping the two in step.** A notebook and its site page are two expressions of the
same material, and they can drift. If you change a notebook, check whether its page
needs the same change — and note that each classical page carries the code twice,
once in Python and once in R, which must agree.

## Licence

MIT — see [LICENSE](LICENSE). Third-party code and data, with the notices their
licences require, are recorded in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Contributing

Found an error? See [CONTRIBUTING.md](CONTRIBUTING.md).
