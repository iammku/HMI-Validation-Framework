"""Instrument Cluster Warning System

Problem Statement:
Build a vehicle health monitoring system that validates:
- Speed
- Fuel
- Seatbelt
- Door
- Ignition

Generate:
- Vehicle Readiness Status
- Active Warning
- Health Score
- Cluster Health Report

Interview Questions:
1. Difference between print() and return()?
2. What is modular programming?
3. What is function communication?
4. What are multiple return values?
5. Why use functions instead of writing all code in one block?
6. How is health score calculated?
7. How does data flow between functions?
8. Explain the execution flow of this project.
"""
def check_speed(speed):
    if speed >= 120:
        updated_speed = speed - 20
        return "Overspeed", updated_speed
    elif speed >= 80:
        return "High Speed", speed
    else:
        return "Normal speed", speed
def check_fuel(fuel, speed):
    if fuel < 20 and speed >= 100:
        return "Critical Warning"
    elif fuel < 20:
        return "Low fuel"
    else:
        return"Fuel Okay"
def check_seatbelt(seatbelt, speed):
    seatbelt=seatbelt.upper()
    if seatbelt == "UNBUCKLED" and speed > 0:
        return "Seatbelt Warning"
    return "Safe Driving"
def check_door(door, speed):
    door=door.upper()
    if door == "OPEN" and speed > 0:
        return "Door Ajar"
    return "Door closed"
def vehicle_ready(ign, door, seatbelt, fuel):
    ign = ign.upper()
    door = door.upper()
    seatbelt = seatbelt.upper()
    if ign == "ON" and door != "OPEN" and seatbelt != "UNBUCKLED" and fuel > 10:
        return "Vehicle Ready"
    return "Vehicle not ready"
def warning_manager(fuel_status,
                    door_status,
                    seatbelt_status,
                    speed_status):
    if fuel_status == "Critical Warning":
        return "Critical Warning"
    elif door_status == "Door Ajar":
        return "Door Warning"
    elif seatbelt_status == "Seatbelt Warning":
        return "Seatbelt warning"
    elif speed_status == "Overspeed":
        return "Speed warning"
    else:
        return "No warnings, Have a safe drive!!"
def health_score(fuel_status,
                    door_status,
                    seatbelt_status,
                    speed_status):
    score = 100
    if fuel_status == "Critical Warning":
        score -= 20
    if door_status == "Door Ajar":
        score -= 10
    if seatbelt_status == "Seatbelt Warning":
        score -= 10
    if speed_status == "Overspeed":
        score -= 20
    return score
def cluster_health_simulator(ign, door, seatbelt, fuel, speed):
    print("\n===== CLUSTER HEALTH REPORT =====")
    if ign.upper() != "ON":
        print("Vehicle Not Ready")
        return
    speed_status, updated_speed = check_speed(speed)

    fuel_status = check_fuel(
        fuel,
        updated_speed
    )
    seatbelt_status = check_seatbelt(
        seatbelt,
        updated_speed
    )
    door_status_result = check_door(
        door,
        updated_speed
    )
    vehicle_status = vehicle_ready(
        ign,
        door,
        seatbelt,
        fuel
    )
    active_warning = warning_manager(
        fuel_status,
        door_status_result,
        seatbelt_status,
        speed_status
    )
    score = health_score(
        fuel_status,
        door_status_result,
        seatbelt_status,
        speed_status
    )
    print(f"Speed Status      : {speed_status}")
    print(f"Current Speed     : {updated_speed}")
    print(f"Fuel Status       : {fuel_status}")
    print(f"Seatbelt Status   : {seatbelt_status}")
    print(f"Door Status       : {door_status_result}")
    print(f"Vehicle Status    : {vehicle_status}")
    print(f"Active Warning    : {active_warning}")
    print(f"Health Score      : {score}/100")
cluster_health_simulator(
    ign="on",
    door="close",
    seatbelt="Buckled",
    fuel=115,
    speed=12
)

