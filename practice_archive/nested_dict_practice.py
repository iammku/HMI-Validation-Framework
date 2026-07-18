"""TC001 -> Overspeed
TC002 -> Normal
TC003 -> Overspeed"""

test_data = {

    "TC001": {
        "speed": 120,
        "fuel": 15,
        "door": "OPEN"
    },

    "TC002": {
        "speed": 80,
        "fuel": 50,
        "door": "CLOSED"
    },

    "TC003": {
        "speed": 140,
        "fuel": 10,
        "door": "OPEN"
    }
}
for keys, values in test_data.items():
    if values["speed"]>=120:
        print(f"{keys} -> Overspeed")
    else:
        print(f"{keys} -> Normal speed")

