# stay-locator

[![Release](https://img.shields.io/github/v/release/connorjoleary/stay-locator)](https://img.shields.io/github/v/release/connorjoleary/stay-locator)
[![Build status](https://img.shields.io/github/actions/workflow/status/connorjoleary/stay-locator/main.yml?branch=main)](https://github.com/connorjoleary/stay-locator/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/connorjoleary/stay-locator/branch/main/graph/badge.svg)](https://codecov.io/gh/connorjoleary/stay-locator)
[![Commit activity](https://img.shields.io/github/commit-activity/m/connorjoleary/stay-locator)](https://img.shields.io/github/commit-activity/m/connorjoleary/stay-locator)
[![License](https://img.shields.io/github/license/connorjoleary/stay-locator)](https://img.shields.io/github/license/connorjoleary/stay-locator)

Test here

- **Github repository**: <https://github.com/connorjoleary/stay-locator/>
- **Documentation** <https://connorjoleary.github.io/stay-locator/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:connorjoleary/stay-locator.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Running your project

Trigger with `uvicorn stay_locator.api.main_api:app --reload` to stand up local server.

TODO: Add to poetry start and trigger programatically

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
