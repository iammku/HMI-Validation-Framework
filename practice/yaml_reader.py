from pathlib import Path
import yaml

project_root= Path(__file__).parent.parent
yaml_config= project_root/"config"/"test_config.yaml"

with yaml_config.open("r",encoding="utf-8") as f:
    config= yaml.safe_load(f)
print(config)
print(config["speed"])
print(config["vehicle"])

