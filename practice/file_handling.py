"""Data-Driven Test Execution & Report Generation
Problem Statement:
Build a mini automation framework that:
- Loads test data
- Validates speed conditions
- Generates PASS/FAIL results
- Counts passed and failed tests
- Generates an execution report"""
import json
test_data = {
    "TC001": {"speed": 120},
    "TC002": {"speed": 80},
    "TC003": {"speed": 140},
    "TC004": {"speed": 60}
}
with open("test_data.json", "w") as f:
    json.dump(test_data, f, indent =4)
def validate_speed(speed):
    if speed>=120:
        return "Fail"
    return "Pass"
def execute_tests(test_data):
    result ={}
    passed=0
    failed=0
    failed_tests=[]
    for tc_id, data in test_data.items():
        status= validate_speed(data["speed"])
        result[tc_id]=status #think it as like adding elements in dict.
        if status=="Pass":
            passed+=1
        else:
            failed+=1
            failed_tests.append(tc_id)
    with open("execution_report.txt", "w") as f:
        f.write("===== EXECUTION REPORT =====")
        for tc_id, data in result.items():
            f.write(f"\n{tc_id} -> {data}")
        f.write(f"\nTotal Tests: {passed+failed}")
        f.write(f"\nPassed: {passed}")
        f.write(f"\nFailed: {failed}")
        return result, failed_tests
result, failed_tests = execute_tests(test_data)
print("Results:")
print(result)
print("\nFailed Tests:")
print(failed_tests)


