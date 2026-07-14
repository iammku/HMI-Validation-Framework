from pathlib import Path
class Vehicle:
    def boot_cluster(self):
        return "Cluster Boot Successful"
    def display_speed(self):
        print("Current Speed : 120")
    def save_cluster_log(self, path:Path):
        log_file=path/"cluster_log.txt"
        log_file.write_text("Cluster Boot Successful")
        return log_file
    def show_warning(self):
        print("Low Fuel Warning")
    def display_theme(self):
        return "Dark Theme"