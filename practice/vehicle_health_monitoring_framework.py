"""
========================================================
DAY 1-5 CAPSTONE PROJECT
Vehicle Health Monitoring Framework
========================================================

Problem Statement

You are a Cluster Test Engineer.

Build a data-driven vehicle health monitoring framework
that validates vehicle conditions and generates a
health report.

Input Data:

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
        "fuel": 50,
        "door": "CLOSED",
        "seatbelt": "BUCKLED",
        "ignition": "ON"
    },

    "TC003": {
        "speed": 140,
        "fuel": 10,
        "door": "OPEN",
        "seatbelt": "UNBUCKLED",
        "ignition": "ON"
    },

    "TC004": {
        "speed": 60,
        "fuel": 5,
        "door": "CLOSED",
        "seatbelt": "BUCKLED",
        "ignition": "OFF"
    }
}

Requirements

1. Create evaluate_testcase(tc_id, data)

2. Generate warnings:
   - Overspeed Warning
   - Low Fuel Warning
   - Door Ajar Warning
   - Seatbelt Warning
   - Ignition OFF Warning

3. Calculate Health Score

   Start Score = 100

   Deductions:
   Overspeed      = -20
   Low Fuel       = -20
   Door Open      = -10
   Seatbelt       = -10
   Ignition OFF   = -30

4. Return:
   {
       "score": score,
       "warnings": warnings
   }

5. Create execute_all_tests()

6. Execute all testcases

7. Create Failed Test List
   Rule:
   Score < 70

8. Create Retry Queue
   Failed Tests + Last Testcase

9. Create Priority Tests
   First Testcase
   Middle Testcase
   Last Testcase

10. Generate Test Execution Report

Bonus

Create Top Risky Tests

Rule:
Score < 50

Concepts Practiced

- Variables
- Conditions
- Functions
- Return Values
- Loops
- Lists
- append()
- extend()
- Dictionaries
- Nested Dictionaries
- Data Driven Testing

Interview Questions

1. Difference between append() and extend()?
2. Why use return instead of print?
3. What is data-driven testing?
4. Difference between list and dictionary?
5. What is a nested dictionary?
6. How does function communication work?
7. How are retry queues created?
8. How would this scale to 1000 testcases?

========================================================
SOLUTION STARTS BELOW
========================================================
"""
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
        "fuel": 50,
        "door": "CLOSED",
        "seatbelt": "BUCKLED",
        "ignition": "ON"
    },

    "TC003": {
        "speed": 140,
        "fuel": 10,
        "door": "OPEN",
        "seatbelt": "UNBUCKLED",
        "ignition": "ON"
    },

    "TC004": {
        "speed": 60,
        "fuel": 5,
        "door": "CLOSED",
        "seatbelt": "BUCKLED",
        "ignition": "OFF"
    }
}
def evaluate_testcase(tc_id, data):
    warnings=[]
    score=100
    if data["speed"] >= 120:
        warnings.append("Overspeed Warning")
        score-=20
    if data["fuel"] <= 20:
        warnings.append("Low Fuel Warning")
        score-=20
    if data["door"] == "OPEN":
        warnings.append("Door Ajar Warning")
        score-=10
    if data["seatbelt"] == "UNBUCKLED":
        warnings.append("Seatbelt Warning")
        score-=10
    if data["ignition"] == "OFF":
        warnings.append("Ignition Warning")
        score-=30
    return {"score": score, "warnings": warnings}
def execute_all_tests(test_data):

    failed_tests = []

    risky_tests = []

    test_ids = list(test_data.keys())

    print("\n===== TEST EXECUTION REPORT =====")

    for tc_id, data in test_data.items():

        result = evaluate_testcase(tc_id, data)

        print(f"\n{tc_id}")

        print(f"Score: {result['score']}")

        print("Warnings:")

        if len(result["warnings"]) == 0:
            print("None")

        else:
            for warning in result["warnings"]:
                print(warning)

        if result["score"] < 70:
            failed_tests.append(tc_id)

        if result["score"] < 50:
            risky_tests.append(tc_id)

        print("----------------")

    retry_queue = []

    retry_queue.extend(failed_tests)

    retry_queue.append(test_ids[-1])

    middle = len(test_ids) // 2

    priority_tests = [
        test_ids[0],
        test_ids[middle],
        test_ids[-1]
    ]

    print("\nFailed Tests:")
    print(failed_tests)

    print("\nRetry Queue:")
    print(retry_queue)

    print("\nPriority Tests:")
    print(priority_tests)

    print("\nTop Risky Tests:")
    print(risky_tests)
execute_all_tests(test_data)