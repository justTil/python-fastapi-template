import os


def get_project_root(marker_file: str = "main.py") -> str:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != "/":
        if marker_file in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    raise FileNotFoundError(
        f"Cannot find {marker_file} in any parent directory.")


# Example usage with default marker file:
root_path = get_project_root()
if root_path:
    print(f"Project root found at: {root_path}")

# Example usage with custom marker file:
root_path = get_project_root(".gitignore")
if root_path:
    print(f"Project root found at: {root_path}")
