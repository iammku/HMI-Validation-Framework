def speed_loop(speed):
    for i in range(0, speed+1, 20):
        if i>120:
            print(f"Overspeed warning: {i}")
            i-=10
            print(f"brake applied: {i}")
        else:
            print(f"Normal speed: {i}")
def fuel_status(fuel):
        if fuel<50:
            print(f"Low Fuel {fuel}")
        else:
            print(f"Normal fuel level {fuel}")
def ign_status(ign):
    if ign=="ON":
        print("Ready to drive")
    else:
        print("Turn on ign")
def vehicle_simulator(speed, fuel, ign):
    speed_loop(speed)
    fuel_status(fuel)
    ign_status(ign)
vehicle_simulator(178,80,"ON")