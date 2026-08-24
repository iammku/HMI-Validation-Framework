def vehicle_input(*args, **kwargs):
    print(args)
    print(kwargs)

vehicle_input(20,10, gear="D", ignition=True)

#Accessing kwargs
def vehicle_info(**kwargs):
    print(kwargs["speed"])
vehicle_info(speed=40)

def vehicle_action(action, *args, **kwargs):
    print(action)
    print(args)
    print(kwargs)

vehicle_action("Brake", "D", Gear="P", speed=56)

# * can be used when calling a function
values1 = (10, 20)
def add(a,b):
    print(a+b)
add(*values1)

values2 = {"gear": "D", "speed":56}
def add1(gear,speed):
    print(gear)
    print(speed)
add1(**values2)