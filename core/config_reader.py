import json
import yaml
from core.logger import logger
from core.paths import CONFIG_DIR
from core.environment import get_environment


class ConfigurationError(Exception):
    """Raised when the framework configuration is invalid."""
    pass

REQUIRED_KEYS = ["vehicle", "ignition", "gear"]

def find_config_file(environment):
    """Locate the configuration file for the given environment.
    Supports YAML and JSON"""
    candidate_paths = [
        CONFIG_DIR / f"{environment}.yaml",
        CONFIG_DIR / f"{environment}.yml",
        CONFIG_DIR / f"{environment}.json",
    ]

    config_path = None

    for path in candidate_paths:
        if path.exists():
            config_path = path
            break
    if config_path is None:
        logger.error(f"Configuration file not found: {environment}")
        raise ConfigurationError(
            f"Missing configuration path {environment}"
        )
    return config_path


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

#config_path=CONFIG_DIR/"test_config.json"
# config_path=CONFIG_DIR/"test_config.yaml"
# if not config_path.exists():
#     logger.error(f"Configuration file not found: {config_path}")
#     raise FileNotFoundError(
#         f"Configuration file not found: {config_path}"
#     )


def load_config(config_path):
    """Load JSON or YAML configuration"""
    try:
        with config_path.open("r", encoding="utf-8") as f:
            if config_path.suffix == ".json":
                return json.load(f)
            elif config_path.suffix in (".yaml", ".yml"):
                return yaml.safe_load(f)
            else:
                logger.error("Unsupported configuration format")
                raise ConfigurationError(
                    "Unsupported configuration format."
                )
    except json.JSONDecodeError as e:
        logger.error(f"Invalid json {config_path} : {e}")
        raise ConfigurationError(f"Invalid JSON in {config_path}") from e
    except yaml.YAMLError as e:
        logger.error(f"Invalid YAML {config_path}: {e}")
        raise ConfigurationError(f"Invalid YAML in {config_path}") from e

def initialize_configuration():
    environment = get_environment()
    config_path = find_config_file(environment)
    config = load_config(config_path)
    validate_required_keys(config)
    validate_values(config)
    logger.info(f"configuration loaded successfully from {config_path}")
    return config

config = initialize_configuration()

def get_config():
    """Return validated configuration"""
    return config