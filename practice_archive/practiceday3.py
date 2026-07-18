def speed_status(speed):
    if speed>=120:
        updated_speed=speed-20
        return "Overspeed", updated_speed
    return "Normal"
def warnings_status(check_s):
    if check_s=="Overspeed":
        return "Critical"
    return "safe"
def health(check_s):
    score=100
    if check_s=="Overspeed":
        score-=20
        return score
def vehicle(speed):
    l=status, new_speed=speed_status(speed)
    w=warnings_status(status)
    h=health(status)
    print(l,w,h)
vehicle(200)