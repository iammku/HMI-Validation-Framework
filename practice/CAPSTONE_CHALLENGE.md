# 🚗 Automotive Framework Capstone (Version 1)

## 📌 Objective

Build a mini **Automotive Cluster Test Execution Framework** using Python concepts learned.

The framework should:

* Read vehicle test data from a JSON file
* Validate vehicle data
* Generate vehicle warnings
* Calculate vehicle health score
* Determine vehicle health status
* Execute all test cases
* Generate an execution report
* Display execution summary

---

# 📚 Concepts Covered

* Variables
* Data Types
* Conditions
* Loops
* Functions
* Lists
* Dictionaries
* Nested Dictionaries
* JSON Handling
* File Handling
* Classes & Objects
* Constructors
* Methods
* Inheritance
* Method Overriding
* `super()`
* Exception Handling
* Git
* Terminal

---

# ✅ Requirement 1 – JSON Test Data

Create a file named:

```
vehicle_test_data.json
```

Store multiple vehicle test cases.

Each test case should contain:

* Speed
* Fuel
* Door
* Seatbelt
* Ignition

Include:

* Healthy Vehicle
* Warning Vehicle
* Critical Vehicle
* Invalid Vehicle (Negative Speed/Fuel)

---

# ✅ Requirement 2 – Load Test Data

Create:

```python
load_test_data()
```

Responsibilities:

* Read JSON file
* Return dictionary
* Handle FileNotFoundError

---

# ✅ Requirement 3 – Parent Class

Create:

```python
class Vehicle
```

Constructor should initialize:

* Speed
* Fuel
* Door
* Seatbelt
* Ignition

---

# ✅ Requirement 4 – Vehicle Validation

Create:

```python
validate_vehicle()
```

Validation Rules:

* Speed < 0 → Raise ValueError
* Fuel < 0 → Raise ValueError

---

# ✅ Requirement 5 – Warning Generation

Create:

```python
generate_warnings()
```

Generate:

* Overspeed
* Low Fuel
* Door Ajar
* Seatbelt Warning
* Ignition OFF

Return warnings as a list.

---

# ✅ Requirement 6 – Health Score

Create:

```python
calculate_health_score()
```

Initial Score:

```
100
```

Deduct:

| Warning          | Score |
| ---------------- | ----: |
| Overspeed        |   -20 |
| Low Fuel         |   -20 |
| Door Ajar        |   -10 |
| Seatbelt Warning |   -10 |
| Ignition OFF     |   -30 |

Return final score.

---

# ✅ Requirement 7 – Health Status

Create:

```python
get_health_status()
```

Return:

* HEALTHY
* WARNING
* CRITICAL

---

# ✅ Requirement 8 – Inheritance

Create:

```python
class ClusterVehicle(Vehicle)
```

Override:

```python
generate_warnings()
```

Use:

```python
super()
```

Additional Rule:

```
Speed >= 150

↓

Critical Cluster Warning
```

---

# ✅ Requirement 9 – Execute Tests

Create:

```python
execute_tests()
```

Responsibilities:

* Create Vehicle Object
* Validate Vehicle
* Generate Warnings
* Calculate Health Score
* Determine Health Status
* Store Results

---

# ✅ Requirement 10 – Result Storage

Create:

```python
results = {}
```

Store:

* Status
* Warnings
* Health Score
* Health Status

---

# ✅ Requirement 11 – Execution Report

Generate:

```
execution_report.txt
```

Include:

* Test Case ID
* Status
* Health Score
* Health Status
* Warnings

---

# ✅ Requirement 12 – Summary

Generate summary containing:

* Total Tests
* Passed
* Failed
* Critical
* Failed Test IDs
* Critical Test IDs

---

# ⭐ Bonus Challenge 1

Create:

```python
failed_tests = []
```

Store all failed test case IDs.

---

# ⭐ Bonus Challenge 2

Create:

```python
critical_tests = []
```

Store all critical test case IDs.

---

# ⭐ Bonus Challenge 3

Sort execution results by Health Score (Highest First).

---

# ⭐ Bonus Challenge 4

Display Statistics:

* Highest Score
* Lowest Score
* Average Score

---

# ⭐ Bonus Challenge 5 (Advanced)

Create another child class:

```python
class ADASVehicle(Vehicle)
```

Override:

```python
generate_warnings()
```

Use:

```python
super()
```

Additional Rule:

```
Speed > 100
AND
Seatbelt == UNBUCKLED

↓

ADAS Collision Risk
```

---

# 📌 Framework Flow

```
JSON
   │
   ▼
load_test_data()
   │
   ▼
execute_tests()
   │
   ▼
Create Vehicle Object
   │
   ▼
Validate Vehicle
   │
   ▼
Generate Warnings
   │
   ▼
Calculate Health Score
   │
   ▼
Get Health Status
   │
   ▼
Store Results
   │
   ▼
Generate Report
   │
   ▼
Generate Summary
```

---

# 🚀 Future Improvements (Version 2): In Progress
