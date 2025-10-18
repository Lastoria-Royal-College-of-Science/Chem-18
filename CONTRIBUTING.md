# Contributing Guidelines

Thanks for your interest in contributing to **Chem 18: Introductory Data Science for Modern Chemists**. We welcome contributions of all kinds: bug reports, documentation, translations, notebooks, and small improvements. See the repository home for context and setup instructions.

---

## How to Open an Issue

If you encounter a bug or have a feature request, please [open an issue](https://github.com/Lastoria-Royal-College-of-Science/Chem-18/issues/new). The issue format is recommended to follow the [Conventional Commends](https://conventionalcomments.org/) specification.

---

## How to Submit a Pull Request

If you want to contribute code, documentation, or translations, please follow these steps:
1. Fork the repository and clone it to your local machine.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Open a pull request.

### Commit Message Style

This project recommends following the [Conventional Commits](https://www.conventionalcommits.org/) specification. Consistent commits make it easier to track changes and generate changelogs automatically.

### Notebook-specific Rules

This repository contains many **Jupyter Notebooks**. To keep the diffs clean and avoid merge conflicts, **clear all outputs** before committing:
- In Jupyter Notebook or JupyterLab: `Edit` -> `Clear Outputs of All Cells`
- In the command line:
  ```shell
  jupyter nbconvert --clear-output --inplace notebooks/01-intro.ipynb
  ```

---

## Code of Conduct

Be respectful and constructive. If you encounter problematic behavior, please contact the maintainers.

---

**Thank you for contributing to Chem 18!**
