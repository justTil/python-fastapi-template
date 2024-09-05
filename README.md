
# FastAPI x Uvicorn Template

This is a small FastAPI x Uvicorn tempalte for developers to get started quickly. The project suggests a simple folder/project structure and some basic helpful utility functions.

## Installation

### Installation after git clone

When setting up the project, run the following command:

```bash
pip install -r requirements.txt
```

When saving the project after adding new packages, run this command:

```bash
pip freeze > requirements.txt
```

## FAQ

### How do I start the FastAPI instance?

If you are using VSCode, you can use the debugpy debugger with three configurations that are defined in the .vscode/launch.json. To run the API with the debugger attached, select the "Python: FastAPI" configuration at the top-left corner of the debugger in VSCode.

### How do I start the FastAPI without the debugger?

Run the following command in the console:

```bash
uvicorn app.main:app --reload --port 8000
```

#### How can I run python files/scripts in general?

Use the "Python: Current File" configuration at the the top-left corner and press F5 (default debug hotkey) and the python program will start in debug mode.

## Feedback

If you have any feedback, please reach out to us at <contact@alatorgenesis.com>

## Authors

- [@justTil](https://github.com/justTil)

## License

[MIT](https://choosealicense.com/licenses/mit/)
