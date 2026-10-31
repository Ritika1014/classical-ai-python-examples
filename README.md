# Classical AI and Python Examples

A collection of small, standalone Python scripts for exploring classical search algorithms and commonly used Python tools for numerical computing, data analysis, statistics, and machine learning.

The examples use hard-coded sample data and print results to the console. The plotting examples open a chart window. There is no single application entry point: run each script separately.

## Contents

### Classical search and optimization

| File | What it demonstrates |
|---|---|
| [`aostar.py`](aostar.py) | A simplified AO* search example on a small AND-OR graph, using heuristic and edge costs. |
| [`astaralgorithm.py`](astaralgorithm.py) | A* graph search with edge costs and heuristic values; prints the path to the goal when found. |
| [`bestfirstsearch.py`](bestfirstsearch.py) | Greedy best-first search using a priority queue ordered by heuristic values. |
| [`breadthfirstsearch.py`](breadthfirstsearch.py) | Breadth-first traversal of a graph until the goal is found. |
| [`depthfirstsearch.py`](depthfirstsearch.py) | Iterative depth-first traversal using a stack. |
| [`hillclimbing.py`](hillclimbing.py) | Hill climbing on a one-dimensional sample objective function. |

### Python, data, and scientific computing

| File | What it demonstrates |
|---|---|
| [`arrayoperations.py`](arrayoperations.py) | NumPy element-wise arithmetic and universal functions. |
| [`numpyarray.py`](numpyarray.py) | Creating and displaying NumPy arrays, zero/one arrays, and ranges. |
| [`linearalgebra.py`](linearalgebra.py) | NumPy matrix multiplication, determinant, and inverse. |
| [`randomnumber.py`](randomnumber.py) | Generating uniform, normally distributed, and integer random values with NumPy. |
| [`statisticalfunctions.py`](statisticalfunctions.py) | Mean, median, standard deviation, and variance with NumPy. |
| [`pandas(datamanipulation).py`](pandas%28datamanipulation%29.py) | Pandas DataFrame creation, selection, filtering, sorting, grouping, and merging. |
| [`handlingmissingvalues.py`](handlingmissingvalues.py) | Examples of filling and dropping missing values in a Pandas DataFrame. |
| [`scipyfunctions.py`](scipyfunctions.py) | SciPy examples for integration, numerical differentiation, root finding, FFT, statistics, and optimization. |
| [`matplotlib(plot).py`](matplotlib%28plot%29.py) | Matplotlib line, bar, scatter, histogram, and pie charts. |
| [`underfittingandoverfitting.py`](underfittingandoverfitting.py) | A scikit-learn polynomial-regression visualization comparing underfitting, a lower-degree fit, and a higher-degree fit. |

## Requirements

- Python 3
- NumPy
- Pandas
- Matplotlib
- SciPy
- scikit-learn

Install the third-party libraries with pip:

```bash
python -m pip install numpy pandas matplotlib scipy scikit-learn
```

## Run an example

From the project directory, run any script with Python. For example:

```bash
python astaralgorithm.py
python numpyarray.py
python "matplotlib(plot).py"
```

On Windows, use `py` instead of `python` if that is how your Python installation is configured:

```powershell
py astaralgorithm.py
py "underfittingandoverfitting.py"
```

The search examples use small graphs defined in their source files. To experiment with different graphs, costs, or heuristic values, edit those sample data structures. The random-number and hill-climbing examples can produce different results on different runs.

## Notes

- These are educational examples rather than a packaged application. Each file runs its demonstration when executed.
- The scripts do not accept command-line arguments or load external datasets.
- Search implementations are intentionally small and use the graphs included in each file; they are not general-purpose pathfinding libraries.
- The plotting scripts require a working graphical display to show their figures.
