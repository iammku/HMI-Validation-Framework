def check_speed(speed):
    if speed>=120:
        updated_speed = speed - 20
        return f"Overspeed, Brake Applied!: {speed}", updated_speed
    elif speed>=100:
        return "High speed"
    else:
        return "Normal Speed"
def check_ign(ign):
    ign=ign.upper()
    if ign=="ON":
        return "Ready to Drive"
    return "Turn on Ign"
def check_fuel(fuel, updated_speed):
    if fuel < 20 and updated_speed > 100:
        return "Critical Warning"
    elif fuel<20:
        return "Low Fuel"
    else:
        return "fuel Ok"
def check_seatbelt(seatbelt, updated_speed):
    seatbelt=seatbelt.upper()
    if seatbelt=="UNBUCKLED" and updated_speed>0:
        return "Seatbelt warnings"
    return "Safe Driving"
def door_status(door, updated_speed):
    door=door.upper()
    if door=="OPEN" and updated_speed>0:
        return "door ajar"
    return "Door closed"
def vehicle_ready(ign, door, seatbelt):
    ign = ign.upper()
    door = door.upper()
    seatbelt = seatbelt.upper()
    if ign=="ON" and door=="CLOSED" and seatbelt =="BUCKLED":
        return "Vehicle Ready"
    return "Vehicle Not Ready"
def cluster_health_simulator(updated_speed, ign, fuel, door, seatbelt):
    print("\n--- Cluster Health Report ---")

    if check_ign(ign)!= "Ready to Drive":
        return "Vehicle not ready"
    else:
        print(f"ignition status: {ign}")
        i = check_speed(updated_speed)
        print(f"Speed status: {i}")
        k=check_fuel(fuel, updated_speed)
        print(f"Fuel status: {k}")
        l=check_seatbelt(seatbelt, updated_speed)
        print(f"Seatbelt status: {l}")
        m=door_status(door, updated_speed)
        print(f"Door status: {m}")
        n= vehicle_ready(ign, door, seatbelt)
        print(f"Vehicle Readiness: {n}")
cluster_health_simulator(123, "ON", 90, "Open", "buckled")

