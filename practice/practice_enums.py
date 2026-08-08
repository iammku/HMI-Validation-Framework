from enum import Enum

class TestStatus(Enum):
    PASS = "1"
    FAIL = "2"
    SKIP = "3"
    RUNNING = 4

    #custome method inside Enum
    def is_finished(self):
#self represents the current state we are checking(e.g. TestStatus.RUNNING)
        return self in (TestStatus.FAIL, TestStatus.SKIP, TestStatus.SKIP)
current_state = TestStatus.RUNNING

if current_state == TestStatus.RUNNING:
    print("Test executing")

current_state = TestStatus.FAIL

if current_state.is_finished():
    print(f"Test concluded with {current_state.name}")
#iterate
for status in TestStatus:
    print(f"{status.name} || {status.value}")

x= TestStatus("3")
print(x)
