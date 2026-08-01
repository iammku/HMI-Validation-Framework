import json
import yaml
from pathlib import Path
from core.logger import logger

class ConfigurationError(Exception):
    """Raised when the framework configuration is invalid."""
    pass

REQUIRED_KEYS = ["vehicle", "ignition"]


def validate_required_keys(config):
    for key in REQUIRED_KEYS:
        if key not in config:
            logger.error(f"Missing required configuration key: {key}")
            raise ConfigurationError(
                f"Missing required configuration key: {key}"
            )


def validate_values(config):
    vehicle = config["vehicle"]
    if vehicle == "":
        logger.error("Vehicle cannot be empty")
        raise ConfigurationError("Vehicle cannot be empty")
    if vehicle is None:
        logger.error("Vehicle cannot be None")
        raise ConfigurationError("Vehicle cannot be None")

current_file=Path(__file__)
# Move from core/ to project root
project_root= current_file.parent.parent

config_path=project_root/"config"/"test_config.json"
#config_path=project_root/"config"/"test_config.yaml"
if not config_path.exists():
    logger.error(f"Configuration file not found: {config_path}")
    raise FileNotFoundError(
        f"Configuration file not found: {config_path}"
    )
#with  open("config_path") as f:
#with config_path.open() as f:
try:
    with config_path.open("r", encoding="utf-8") as f:
        if config_path.suffix == ".json":
            config = json.load(f)
        elif config_path.suffix in (".yaml", ".yml"):
            config = yaml.safe_load(f)
        else:
            logger.error("Unsupported configuration format")
            raise ConfigurationError(
                "Unsupported configuration format."
            )
        #config = json.load(f)
        validate_required_keys(config)
        validate_values(config)
        logger.info(f"configuration loaded successfully from {config_path}")
        #print("Config loaded successfully!")
except json.JSONDecodeError as e:
    logger.error(f"Invalid json {config_path} : {e}")
    raise ConfigurationError(f"Invalid JSON in {config_path}") from e
except yaml.YAMLError as e:
    logger.error(f"Invalid YAML {config_path}: {e}")
    raise ConfigurationError(f"Invalid YAML in {config_path}") from e


def get_config():
    return config