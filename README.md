# Pattern-Outlier

Pattern-Outlier is a Python library for detecting outliers based on frequent pattern mining, inspired by the `fpmoutliers` R package. The package supports multiple algorithms and allows users to dynamically calculate the most reasonable threshold and support parameters.



## Features
- **Support for Multiple Algorithms**: Choose from FPI, WFPI, FPOF, and FPCOF methods for outlier detection.
- **Dynamic Parameter Calculation**: Automatically find the best support and threshold parameters.
- **Model Persistence**: Save and load fitted models for reuse.
- **Flexible Input Handling**: Accepts transaction data in list format.
- **Easy to Use API**: Simple and intuitive interface for fitting models and predicting outliers.


## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.


## Project on PyPI

You can find this project on PyPI at the following link:
[Pattern-Outlier on PyPI](https://pypi.org/project/pattern-outlier/)


## Installation

```bash
pip install -r requirements.txt
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

## References
- He, Z., Xu, X., Huang, J. Z., Deng, S.: FP-Outlier: Frequent Pattern Based Outlier Detection. Computer Science and Information Systems, Vol. 2, No. 1, 103-118. (2005).

- Tang, X., Li, G., Chen, G.: Fast Detecting Outliers over Online Data Streams. 2009 International Conference on Information Engineering and Computer Science, Wuhan, 2009, pp. 1-4.

- Kuchar, J., Svatek, V.: Spotlighting Anomalies using Frequent Patterns. Proceedings of the KDD 2017 Workshop on Anomaly Detection in Finance, Halifax, Nova Scotia, Canada, PMLR, 2017.
