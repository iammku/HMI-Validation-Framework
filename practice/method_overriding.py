"""
INHERITANCE & METHOD OVERRIDING

Objective:
Learn how child classes inherit attributes and methods from parent classes.

Requirements:
1. Create a parent Vehicle class.
2. Create child classes:
   - ClusterVehicle
   - IVIVehicle
   - ADASVehicle
3. Demonstrate inherited methods and attributes.
4. Override a parent method in child class.
5. Use super() to access parent implementation.
6. Add child-specific functionality.
"""
class Vehicle:
    def __init__(self, speed, fuel):
        self.speed=speed
        self.fuel=fuel
    def check_health(self):
        warnings=[]
        if self.speed >= 120:
            warnings.append("Overspeed")
        if self.fuel <= 20:
            warnings.append("Low Fuel")
        if len(warnings) == 0:
            warnings.append("Healthy")
        return warnings
class ClusterVehicle(Vehicle):
    def check_health(self):
        warn=super().check_health()
        if self.speed >= 150:
            print("Critical Cluster Warning")
            return
        print("===== CLUSTER STATUS =====")
        for warning in warn:
            print(warning)
cluster1 = ClusterVehicle(160, 50)
cluster2 = ClusterVehicle(130, 15)
cluster3 = ClusterVehicle(80, 50)
cluster1.check_health()
cluster2.check_health()
cluster3.check_health()