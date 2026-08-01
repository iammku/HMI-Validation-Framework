from core.config_reader import get_config

config=get_config()


def show_cluster_info():
    print(config["vehicle"])
    print(config["speed"])
    print(config["gear"])
    print(config["theme"])