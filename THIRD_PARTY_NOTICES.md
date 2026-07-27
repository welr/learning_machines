# Third-party notices

Verified 2026-07-27.

## Code

**`ch12_01_build_a_gpt.ipynb`** follows the architecture, structure and naming of
Andrej Karpathy's "Let's build GPT" lecture code and nanoGPT, with the code
rewritten in the book's notation. Both upstream repositories are MIT licensed —
`karpathy/nanoGPT` by a `LICENSE` file, `karpathy/ng-video-lecture` by a statement
in its README (GitHub's license detector reports "none" for the latter because
there is no `LICENSE` file; the README is the operative grant).

> MIT License
> Copyright (c) 2022 Andrej Karpathy
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of
> this software and associated documentation files (the "Software"), to deal in the
> Software without restriction, including without limitation the rights to use,
> copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
> Software, and to permit persons to whom the Software is furnished to do so,
> subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
> FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
> COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
> AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
> WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Data fetched at run time

None of these are redistributed here; each notebook downloads what it needs.

| Data | Used by | Terms |
|---|---|---|
| Tiny Shakespeare (`input.txt`) | `ch12_01` | MIT via `karpathy/ng-video-lecture`; the underlying Shakespeare text is public domain |
| *The Wealth of Nations* | `ch12_01` | Public domain. The loader strips Project Gutenberg's header and footer, which is the condition PG sets for using the underlying work free of its trademark license. See the note below. |
| Fashion-MNIST | `ch09_02`, `ch10_02`, `ch13_01` | MIT, © 2017 Zalando SE |
| California housing | `ch02_04` | Public; derived from Pace & Barry (1997), StatLib |
| auto-mpg (OpenML id 196) | `ch02_04` | OpenML licence field: "Public"; originally UCI |
| Breast cancer (WDBC) | `ch06_02`, `ch08_03` | Bundled with scikit-learn; UCI, CC BY 4.0 |
| Pima diabetes (OpenML "diabetes", id 37) | `ch04_03` | OpenML licence field: "Public". See the note below. |
| MNIST | `ch10_01` | via torchvision; CC BY-SA 3.0 |

### Note — Project Gutenberg

`load_gutenberg` fetches from `gutenberg.org` with a browser User-Agent string.
Project Gutenberg's Terms of Use ask that automated clients not scrape the main
site and direct them to the mirrors instead. Readers running the optional cell may
be rate-limited or blocked. Prefer a mirror, or host the stripped text alongside
the notebook.

### Note — Pima diabetes

This dataset records members of the Akimel O'odham (Pima) community, gathered in a
long-running NIH study. Its circulation as a generic ML benchmark has been
criticised on research-ethics grounds, independently of its licence status. Worth a
sentence of context wherever it is used, or substitution with another clinical
dataset.

## Python dependencies

All permissive; no copyleft. numpy (BSD-3/0BSD/MIT/Zlib/CC0), pandas (BSD-3),
matplotlib (PSF), scipy (BSD-3), scikit-learn (BSD-3), torch and torchvision
(BSD-3), pymc (Apache-2.0), arviz (Apache-2.0), IPython (BSD-3).
