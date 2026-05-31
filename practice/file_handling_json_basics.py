"""
Day 6 Part 1

File Handling & JSON Basics

Problem Statement:
Learn how to:
- Create text files
- Read text files
- Write JSON files
- Read JSON files
- Access JSON data
- Store test data externally

Exercises:
1. Create vehicle_report.txt
2. Read vehicle_report.txt
3. Write vehicle dictionary to vehicle.json
4. Read vehicle.json
5. Load test data from JSON and validate overspeed conditions

Concepts Practiced:
- with open()
- read()
- write()
- writelines()
- json.load()
- json.dump()
- Nested Dictionary Access
- External Test Data Management

Interview Questions:
1. Difference between read() and readline()?
2. Difference between write() and writelines()?
3. Why use with open()?
4. Difference between JSON and Python Dictionary?
5. Difference between json.load() and json.dump()?
6. What does indent=4 do?
7. How do you access nested JSON data?
8. Why store test data in JSON instead of hardcoding?
"""
import json
lines="Vehicle Ready", "\nDoor Closed", "\nFuel Level Normal"
with open ("vehicle_report.txt","w") as f:
    f.writelines(lines)
with open ("vehicle_report.txt", "r") as f:
    content=f.read()
    print(content)

vehicle={"fuel":50,
         "door":"OPEN",
         "speed":120}
with open ("vehicle.json", "w") as f:
    json.dump(vehicle, f, indent=4)
with open ("vehicle.json", "r") as f:
    data=json.load(f)
    for keys in data:
        print(keys)
#Challange problem
test_data={
    "TC001":{"speed":120},
    "TC002":{"speed":80},
    "TC003":{"speed":140}
}
with open("test_data.json", "w") as f:
    json.dump(test_data, f, indent=4)
with open("test_data.json","r") as f:
    data= json.load(f)
    for keys, values in data.items():
        if values["speed"]>=120:
            print(f"Overspeed-> {keys}")
        else:
            print(f"Normal Speed-> {keys}")