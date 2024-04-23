# Experiment with Image Generation - DALL-E

Experiment with Open AI's Dall-E to generate images.

## Acknowledgements

Many thanks ❤️ go to

- [JetBrains](https://www.jetbrains.com/?from=PROJECT-NAME) who provide an [Open Source License](https://www.jetbrains.com/community/opensource/) for this project

## Developer Guide

### Prerequisites

It is recommended to use a python virtual environment. Create and activate it:

```shell
python3 -m venv venv
source venv/bin/activate
```

Install the required python packages:

```shell
pip install -r requirements.txt
```

Then install this package in development mode:

```shell
pip install --editable .
```

### `python src/dall_e/main.py`

Run the application.

### `python -m pytest`

Execute the tests once.

### `ptw . --now --last-failed --new-first`

Launches the test runner in the interactive watch mode.
