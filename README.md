# Some python project templates I created for my personal use


## Contents

### Package

Generates python package with:

* `pytest` as test runner
* `flake8` as linter
* `mypy` as type checker
* `black` as code formatter
* `pyproject.toml` for specifying dependencies and tool settings (except flake8 which is configured in `.flake8` file)
* Optionally, Dockerfile and docker-compose.yml for running tests in isolated environment along with some helper scripts
* Optionally, pytest-cov for reporting test coverage


## Usage

In order to generate project from one of the templates, make sure you have `cookiecutter` installed and run
```
cookiecutter https://github.com/mpaliwoda/cookiecutter-python --directory=${directory_name}
```
where `${directory_name}` is name of the template you wish to use, e.g.
```
cookiecutter https://github.com/mpaliwoda/cookiecutter-python --directory=package
```


## TODO

Work somewhat planned for the future:

* Expand pypackage for open source usage
* Add fastapi project template
* Add flask project template
