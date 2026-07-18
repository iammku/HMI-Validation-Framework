#follow CAPSTONE_CHALLENGE.md
import json
import json
test_data = {
    "TC001": {
        "speed": 130,
        "fuel": 15,
        "door": "OPEN",
        "seatbelt": "BUCKLED",
        "ignition": "ON"
    },
    "TC002": {
        "speed": 80,
        "fuel": 60,
        "door": "CLOSED",
        "seatbelt": "BUCKLED",
        "ignition": "ON"
    },
    "TC003" : {
        "speed": 140,
        "fuel": 10,
        "door": "OPEN",
        "seatbelt": "UNBUCKLED",
        "ignition": "OFF"
    },
    "TC004" : {
        "speed": -20,
        "fuel": 50,
        "door": "CLOSED",
        "seatbelt": "BUCKLED",
        "ignition": "ON"
    }
}
with open("vehicle_test_data.json", "w") as f:
    json.dump(test_data, f, indent=4)

def load_test_data():
    try:
        with open ("vehicle_test_data.json", "r") as f:
            data=json.load(f)
        return data
    except FileNotFoundError:
        print("test_data not available")
class Vehicle:
    def __init__(self, speed, fuel, door, seatbelt, ignition):
        self.speed=speed
        self.fuel=fuel
        self.door=door
        self.seatbelt=seatbelt
        self.ignition=ignition
    def validate_vehicle(self):
        try:
            if self.speed < 0:
                raise Exception
            if self.fuel < 0:
                raise Exception
        except ValueError:
            print("invalid value")
    def generate_warnings(self):
        warnings=[]
        if self.speed >=120:
            warnings.append("Overspeed")
        if self.fuel <=20:
            warnings.append("Low fuel")
        if self.door=="OPEN":
            warnings.append("Door ajar")
        if self.seatbelt=="UNBUCKLED":
            warnings.append("Seatbelt warning")
        if self.ignition=="OFF":
            warnings.append("Ignition off")
        return warnings
    def health_score(self):
        score=100
        warning=self.generate_warnings()
        if "Overspeed" in warning:
            score=-20
        if "Low fuel" in warning:
            score=-20
        if "Door ajar" in warning:
            score=-10
        if "Seatbelt warning" in warning:
            score=-10
        if "Ignition Off" in warning:
            score-=30
        return score
    def health_status(self):
        score=self.health_score()
        if score>=80:
            return "Healthy"
        elif score>=50:
            return "Warning"
        else:
            return "Critical"
class ClusterVehicle(Vehicle):
    def generate_warnings(self):
        warnings=super().generate_warnings()
        if self.speed>=150:
            warnings.append("Critical cluster warning")
def execute_tests(data):
    results = {}
    passed = 0
    failed = 0
    critical = 0
    failed_tests = []
    critical_tests = []
    with open ("execution_report.txt", "w") as f:
        f.write("===Execution Report===\n")
        for tc, data in data.items():
            vehicle=Vehicle(data)
            vehicle.validate_vehicle()
            g1=vehicle.generate_warnings()
            h1=vehicle.health_score()
            hs=vehicle.health_status()
            if len(g1)==0:
                passed+=1
                status="pass"
            else:
                failed+=1
                status="fail"
                failed_tests.append(tc)
            if hs=="Critical":
                critical+=1
                critical_tests.append(tc)
            results[tc]={
                "Status": status,
                "Warnings": g1,
                "Score": h1,
                "health":hs
            }
            f.write(f" test case id: {tc}\n")
            f.write(f"test cases status: {status}\n")
            f.write(f" Health score: {h1}\n")
            f.write(f" Health status: {hs}\n")
            f.write(f"Warnings: \n")
            for warn in g1:
                f.write(f"{warn}\n")
            f.write("==================")
            f.write(f"===Summary===\n")
            f.write(f"Total test= {passed+failed}\n")
            f.write(f"Passed test= {passed}\n")
            f.write(f"Failed test= {failed}\n")
            for c1 in critical_tests:
                f.write(f"Critical test:{c1}")
            for f1 in failed_tests:
                f.write(f"Failed test:{f1}")