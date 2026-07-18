"""
Vehicle Health Assessment Framework

Problem Statement:
Build a data-driven vehicle validation framework that:

1. Reads vehicle test data
2. Validates multiple vehicle signals
3. Generates warnings
4. Calculates health score
5. Determines health status
6. Generates execution report
7. Tracks failed testcases
8. Tracks critical vehicles
9. Generates execution summary

Signals:
- Speed
- Fuel
- Door
- Seatbelt
- Ignition

Health Score Rules:
Overspeed         -20
Low Fuel          -20
Door Ajar         -10
Seatbelt Warning  -10
Ignition OFF      -30

Health Status:
>=80  -> HEALTHY
>=50  -> WARNING
<50   -> CRITICAL
"""
import json
vehicle_test_data = {
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
    "TC003": {
        "speed": 140,
        "fuel": 10,
        "door": "OPEN",
        "seatbelt": "UNBUCKLED",
        "ignition": "OFF"
    }
}
with open("vehicle_test_data.json", "w") as f:
    json.dump(vehicle_test_data, f, indent=4)
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
    print("===== VEHICLE REPORT =====")
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
        print("\n")
        print(tc_id)
        print(f"\nStatus:{status}\n")
        print(f"Health Score: {score}\n")
        print(f"Health Status: {health_status}\n")
        print("Warnings:")
        if len(warnings)==0:
            print("None")
        else:
            for warn in warnings:
                print(f"{warn}")
        print("----------------------")
    print("===== SUMMARY =====")
    print(f"Total Tests: {passed+failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print("Failed Tests :")
    for tc in failed_tests:
        print(tc)
    print("Critical Tests:")
    for tc in critical_tests:
        print(tc)
execute_tests(vehicle_test_data)