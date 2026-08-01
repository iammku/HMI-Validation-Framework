import yaml
with open("test_config.yaml", "r", encoding="utf-8") as f:
    config= yaml.safe_load(f)
    print(config)
    print(type(config))
    print(config["vehicle"])
    print(config["speed"])
    print(config["theme"])
    print(config["ignition"])