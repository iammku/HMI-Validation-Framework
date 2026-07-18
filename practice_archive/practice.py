def speed_loop(speed):
    for i in range(1, speed+1, 30):
        if i>120:
            print(f"Overspeed warning: {i}")
            i-=10
            print(f"brake applied: {i}")
        else:
            print(f"Normal speed: {i}")
def fuel_status(fuel):
        while fuel>0:
            if fuel<40:
                print(f"Low fuel: {fuel}")
            else:
                print(f"Fuel level Normal: {fuel}")
            fuel -= 10
        print("fuel empty")
def ign_status(ign):
    ign=ign.upper()
    if ign=="ON":
        print("Ready to drive")
        return True
    else:
        print("Turn on ign")
        return False
def door_status(door, speed):
    door=door.upper()
    if door=="OPEN" and speed>0:
        print("Close the door")
    else:
        print("Safe Driving")
#controller function
def vehicle_simulator(speed, fuel, ign, door):
    ign_on=ign_status(ign)
    if ign_on:
        speed_loop(speed)
        fuel_status(fuel)
        door_status(door, speed)
    else:
        print("No vehicle simulation")
vehicle_simulator(178,30,"on","OpEn")