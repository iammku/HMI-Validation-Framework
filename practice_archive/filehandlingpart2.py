"""Build a Pure JSON-Driven Vehicle Health Framework.

Requirements:
1. Load vehicle test data from JSON.
2. Validate vehicle signals.
3. Generate warnings.
4. Calculate health score.
5. Determine health status.
6. Generate PASS/FAIL result.
7. Track failed testcases.
8. Track critical vehicles.
9. Generate execution report.
10. Separate data from code."""
import json
#with commented below code create a json file
# vehicle_test_data = {
#     "TC001": {
#         "speed": 130,
#         "fuel": 15,
#         "door": "OPEN",
#         "seatbelt": "BUCKLED",
#         "ignition": "ON"
#     },
#     "TC002": {
#         "speed": 80,
#         "fuel": 60,
#         "door": "CLOSED",
#         "seatbelt": "BUCKLED",
#         "ignition": "ON"
#     },
#     "TC003": {
#         "speed": 140,
#         "fuel": 10,
#         "door": "OPEN",
#         "seatbelt": "UNBUCKLED",
#         "ignition": "OFF"
#     }
# }
# with open("vehicle_test_data.json", "w") as f:
#     json.dump(vehicle_test_data, f, indent=4)
def load_test_data():
    with open ("vehicle_test_data.json", "r") as f:
        test_data= json.load(f)
    return test_data
def validate_vehicle(data):
    warnings=[]
    if data["speed"] >= 120:
        warnings.append("Overspeed")
    if data["fuel"] <=15:
        warnings.append("Low Fuel")
    if data["door"] == "OPEN":
        warnings.append("door ajar")
    if data["seatbelt"] == "UNBUCKLED":
        warnings.append("Seatbelt Warning")
    if data["ignition"] == "OFF":
        warnings.append("Ignition OFF")
    return warnings
def calculate_health_score(warnings):
    score=100
    if "Overspeed" in warnings:
        score-=20
    if "Low Fuel" in warnings:
        score-=20
    if "door ajar" in warnings:
        score-=10
    if "Seatbelt Warning" in warnings:
        score-=10
    if "Ignition OFF" in warnings:
        score-=30
    return score
def get_health_status(score):
    if score >= 80:
        return "Healthy"
    elif score >= 50:
        return "WARNING"
    else:
        return "CRITICAL"
def execute_tests(test_data):
    passed=0
    failed=0
    failed_tests = []
    critical_tests=[]
    with open ("execution_report.txt","w") as f:
        f.write("===== VEHICLE REPORT =====")
        for tc_id, data in test_data.items():
            warnings=validate_vehicle(data)
            score=calculate_health_score(warnings)
            health_status=get_health_status(score)
            if health_status=="CRITICAL":
                critical_tests.append(tc_id)
            if len(warnings)==0:
                status="PASS"
                passed+=1
            else:
                status="FAIL"
                failed+=1
            if status=="FAIL":
                failed_tests.append(tc_id)
            f.write("\n")
            f.write(tc_id)
            f.write(f"\nStatus:{status}\n")
            f.write(f"Health Score: {score}\n")
            f.write(f"Health Status: {health_status}\n")
            f.write("Warnings:\n")
            if len(warnings)==0:
                f.write("None")
            else:
                for warn in warnings:
                    f.write(f"{warn}\n")
            f.write("\n----------------------\n")
        f.write("\n===== SUMMARY =====\n")
        f.write(f"Total Tests: {passed+failed}\n")
        f.write(f"Passed: {passed}\n")
        f.write(f"Failed: {failed}\n")
        f.write("Failed Tests :\n")
        for tc in failed_tests:
            f.write(f"{tc}\n")
        f.write("Critical Tests:\n")
        for tc in critical_tests:
            f.write(tc)
test_data=load_test_data()
execute_tests(test_data)