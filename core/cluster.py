class Cluster:
    def __init__(self, config):
        self.config=config

    def show_cluster_info(self):
        print(self.config["vehicle"])
        print(self.config.get("speed", "Unknown"))
        print(self.config.get("gear"))
        print(self.config["theme"])