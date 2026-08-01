import json
from pathlib import Path
import os

print("Current Working Directory:")
print(os.getcwd())

print("\nCurrent File:")
print(__file__)

print("\nPath Object:")
print(Path(__file__))

#current path
print(Path.cwd())

#location of current python file
current_file=Path(__file__)
#current_directory_path
print(current_file.parent)
#parent of current_directory_path
print(current_file.parent.parent)
print("File name without extension:", current_file.stem)
print("File name with extension:", current_file.suffix)
print("Absolute path:", current_file.resolve())
print("Exists:", current_file.exists())
print("Is File:", current_file.is_file())
print("Is Directory:", current_file.is_dir())
config_path= current_file.parent.parent / "config" / "test_config.json"
print("Config path:", config_path)
print("Config Exists:", config_path.exists())
with config_path.open() as f:
    print(json.load(f))