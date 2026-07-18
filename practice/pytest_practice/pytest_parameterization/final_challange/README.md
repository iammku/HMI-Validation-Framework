# Project Structure

```
Cluster_Health_Validation_Framework/

│
├── vehicle.py
├── conftest.py
├── test_cluster.py
├── test_dashboard.py
└── README.md
```

---

# Requirements

## Part A – Vehicle Class

### Requirement 1

Create a class named **Vehicle**.

Constructor should accept:

- speed
- fuel
- battery
- door
- seatbelt
- ignition

Store all values as instance variables.

---

### Requirement 2

Create a method:

```
is_overspeed()
```

Rules:

- Speed > 120 → True
- Otherwise → False

---

### Requirement 3

Create a method:

```
calculate_health_score()
```

Initial score:

```
100
```

Deduct score according to the following rules.

| Condition | Score Deduction |
|------------|----------------:|
| Fuel <= 20 | -20 |
| Battery <= 30 | -20 |
| Door OPEN | -10 |
| Seatbelt UNBUCKLED | -10 |
| Ignition OFF | -30 |

Return the final score.

---

### Requirement 4

Create:

```
health_status()
```

Rules:

| Score | Status |
|--------|---------|
| >=80 | Healthy |
| 50-79 | Warning |
| <50 | Critical |

---

### Requirement 5

Create:

```
generate_warnings()
```

Return a list of active warnings.

Possible warnings:

- Low Fuel
- Battery Low
- Door Ajar
- Seatbelt Warning
- Ignition OFF
- Overspeed

Example:

```python
[
    "Low Fuel",
    "Battery Low"
]
```

---

# Part B – Fixtures

### Requirement 6

Create:

```
can_connection()
```

Fixture

Scope:

```
session
```

Use **yield**

Expected Flow:

```
Opening CANoe...

↓

yield

↓

Closing CANoe...
```

---

### Requirement 7

Create

```
logger(can_connection)
```

Scope

```
module
```

Use fixture dependency.

Expected Flow

```
Logger Started

↓

yield

↓

Logger Closed
```

---

### Requirement 8

Create

```
vehicle(logger)
```

Scope

```
function
```

Create a default vehicle object.

Example values:

- Speed =120
- Fuel =20
- Battery =30
- Door = CLOSED
- Seatbelt = BUCKLED
- Ignition = ON

Use

```
yield
```

Expected Flow

```
Vehicle Boot

↓

yield

↓

Vehicle Shutdown
```

---

### Requirement 9

Create fixture:

```
expected_vehicle()
```

Return:

```python
{
    "speed":120,
    "fuel":20,
    "battery":30,
    "door":"CLOSED",
    "seatbelt":"BUCKLED",
    "ignition":"ON"
}
```

Use this fixture instead of hardcoding expected values.

---

# Part C – Cluster Tests

Create:

```
test_cluster.py
```

---

### Requirement 10

Validate all default vehicle values using

- vehicle fixture
- expected_vehicle fixture

---

### Requirement 11

Write a parameterized test for

```
is_overspeed()
```

Datasets

| Speed | Expected |
|--------|----------|
|80|False|
|100|False|
|120|False|
|130|True|
|150|True|

Use meaningful ids.

---

### Requirement 12

Write another parameterized test for

```
health_status()
```

Datasets

| Fuel | Battery | Door | Seatbelt | Ignition | Expected |
|------|---------|------|-----------|-----------|----------|
|80|80|CLOSED|BUCKLED|ON|Healthy|
|20|80|CLOSED|BUCKLED|ON|Warning|
|10|10|OPEN|UNBUCKLED|OFF|Critical|
|60|20|CLOSED|BUCKLED|ON|Warning|

Use ids.

---

### Requirement 13

Write a test

```
test_warning_list()
```

Validate

```
generate_warnings()
```

---

# Part D – Dashboard Tests

Create

```
test_dashboard.py
```

Write tests for

- Dashboard Theme
- Cluster Ready
- Warning Popup

Reuse the vehicle fixture.