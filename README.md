# Pattern-Outlier

Pattern-Outlier is a Python library for detecting outliers based on frequent pattern mining, inspired by the `fpmoutliers` R package.


## Features
- Identify outliers in transaction data based on frequent pattern mining
- Easy to use and integrate with pandas DataFrames


## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.


## Project on PyPI

You can find this project on PyPI at the following link:
[Pattern-Outlier on PyPI](https://pypi.org/project/pattern-outlier/)


## Acknowledgments

This project is based on the `fpmoutliers` R package by Jaroslav Kuchar and Vojtěch Svátek. Original R package can be found [here](https://github.com/jaroslav-kuchar/fpmoutliers).


## Installation

```bash
pip install -r requirements.txt
```


## Example Usage

```python
import pandas as pd
from src.pattern_outlier.fpoff import FPOF

# Create some dummy data
data = {
    'Bread': [1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    'Milk': [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    'Diapers': [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    'Beer': [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    'Eggs': [1, 0, 0, 1, 0, 1, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

# Convert the data to boolean types as recommended
df = df.astype(bool)

# Initialize and fit the FPOF model
fpof = FPOF(min_support=0.3)
fpof.fit(df)

# Score the data
scores = fpof.score(df)
df['outlier_score'] = scores

# Predict outliers
threshold = 2
predictions = fpof.predict(df, threshold)
df['outlier'] = predictions

# Print the results
print("DataFrame with Outlier Scores and Predictions:")
print(df)

```


## How to Contribute

Contributions from the community are welcome! Here are some guidelines to help you get started:


### Reporting Bugs

If you find a bug, please report it by opening an issue on the [GitHub repository](https://github.com/lihangalex/pattern-outlier/issues). Include as much detail as possible, such as steps to reproduce the bug, the expected behavior, and screenshots if applicable.


### Suggesting Features

If you have an idea for a new feature, please open an issue on the [GitHub repository](https://github.com/lihangalex/pattern-outlier/issues) and describe your idea in detail. Explain why it would be useful and how it should work.


### Submitting Pull Requests

If you'd like to contribute code, please follow these steps:

1. **Fork the repository**: Click the "Fork" button at the top of the repository page on GitHub.

2. **Clone your fork**: Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/lihangalex/pattern-outlier.git
   cd pattern-outlier
   ```

3. **Create a branch**: Create a new branch for your work.
   ```bash
   git checkout -b feature-branch
   ```


4. **Make your changes**: Make your changes to the codebase.

5. **Commit your changes**: Commit your changes with a clear and concise commit message.
    ```bash
    git add .
    git commit -m "Add feature or fix bug"
    ```

6. ***Push your changes***: Push your changes to your forked repository.
   ```bash
   git push origin feature-branch
   ```

7. **Open a pull request**: Go to the original repository and open a pull request from your forked repository. Provide a clear description of your changes and any relevant information.


### Code Style and Guidelines

- Follow the existing code style and conventions used in the project.
- Write clear, concise, and descriptive commit messages.
- Include comments and docstrings to explain your code where necessary.
- Ensure your changes do not break existing tests and write new tests if applicable.


### Running Tests

To run the tests locally, use the following command:

```bash
pytest
```
