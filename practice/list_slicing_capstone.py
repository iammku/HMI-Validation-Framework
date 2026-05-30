"""
Problem Statement:

Build a mini test execution framework using list slicing.

Requirements:
1. Create Smoke Suite (first 2 testcases)
2. Create Regression Suite (middle testcases)
3. Create Sanity Suite (last 2 testcases)
4. Create Failed Test Queue
5. Create Retry Queue
6. Print First and Latest Failed Test
7. Create Priority Test List
8. Execute Testcases in Batches

Concepts Practiced:
- List Indexing
- Negative Indexing
- Slicing
- Functions
- Loops
- append()
- extend()
- Test Suite Selection

Interview Questions:
1. Difference between append() and extend()
2. Difference between indexing and slicing
3. What does [::-1] do?
4. What does [2:-2] mean?
5. Why use negative indexing?
"""

test_cases = [
    "TC001", "TC002", "TC003", "TC004", "TC005",
    "TC006", "TC007", "TC008", "TC009", "TC010",
    "TC011", "TC012", "TC013", "TC014", "TC015"
]
def execute_suite(test_cases):
    print("===== Smoke Suite =====")
    for tc in test_cases[:2]:
        print(tc)
    print("===== Regression Suite =====")
    for tc in test_cases[2:13]:
        print(tc)
    print("===== Sanity Suite =====")
    for tc in test_cases[13:]:
        print(tc)
    print(f"Length of Sanity Suite: {len(test_cases[13:])}")
    print(f"Length of Regression Suite: {len(test_cases[2:13])}")
    print(f"Length of Smoke Suite: {len(test_cases[:2])}")
execute_suite(test_cases)
failed_tests=test_cases[3:8]
print("Failed Cases")
for tc in failed_tests:
    print(tc)
failed_tests.extend(test_cases[13:])
print("Retry Queue")
for tc in failed_tests:
    print(tc)
print("First Failed Test:")
print(failed_tests[0])
print("Latest Failed Test:")
print(failed_tests[-1])
def priority_tests(test_cases):
    for tc in test_cases[:1]:
        print(tc)
    middle_testcase=len(test_cases)//2
    print(test_cases[middle_testcase])
    for tc in test_cases[-1:]:
        print(tc)
priority_tests(test_cases)
def batch_execution(test_cases):
    print("Batch 1")
    for tc in test_cases[0:5]:
        print(tc)
    print("Batch 2")
    for tc in test_cases[5:10]:
        print(tc)
    print("Batch 3")
    for tc in test_cases[10:]:
        print(tc)
batch_execution(test_cases)
