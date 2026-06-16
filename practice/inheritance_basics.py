class Vehicle:
    def __init__(self,speed, fuel):
        self.speed=speed
        self.fuel=fuel
    def show_info(self):
        print(self.fuel)
        print(self.speed)
    def check_health(self):
        has_warning=False
        if self.speed>=120:
            print("Overspeed")
            has_warning=True
        if self.fuel<=20:
            print("Low fuel")
            has_warning=True
        if not has_warning:
            return "No warnings"
        else:
            return "Cluster Warning Active"
class ClusterVehicle(Vehicle):
    def show_cluster_warning(self):
        warn=self.check_health()
        print(warn)
class IVIVehicle(Vehicle):
    def show_media_status(self):
        print("Bluetooth Connected")
cluster = ClusterVehicle(120, 20)
ivi = IVIVehicle(80, 40)
cluster.show_cluster_warning()
cluster.show_info()
ivi.show_media_status()
ivi.show_info()

