import json
import os
from json import JSONDecodeError
from pathlib import Path

class ConfigurationError(Exception):
    """This is used to raise exception for config"""

#from core.config_reader import config_path

print("Current Working Directory:")
print(os.getcwd())

config_path= Path(__file__).parent.parent/"config"/"test_config.json"

if not config_path.exists():
    raise FileNotFoundError(f"json file is not available {config_path}")

try:
    with config_path.open("r", encoding="utf-8") as f:
        config = json.load(f)
    print(f"Vehicle:{config["vehicle"]}")
    print(f"Speed:{config["speed"]}")
    print(f"Gear:{config["gear"]}")
    print(f"Theme:{config["theme"]}")
    config["speed"]=1800
    print(config)
    print(type(config))
    with config_path.open("w",encoding="utf-8") as f:
        json.dump(config,f, indent=4)
    for key, value in config.items():
        print(f" Keys: {key}")
        print(f"Value is:{value}")
except JSONDecodeError as e:
    raise ConfigurationError(f"Invalid JSON in {config_path}") from e