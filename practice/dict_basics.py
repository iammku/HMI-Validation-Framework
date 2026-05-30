cluster_data = {
    "speed:": 130,
    "fuel:": 30,
    "door:": "OPEN",
    "Seatbelt:": "BUCKLED",
    "Ign:": "ON"
}
print(cluster_data.get("Name", "Not Found!"))
#add
cluster_data["Warnings:"]="Door ajar"
#update
cluster_data["door:"]="Close"
#update
cluster_data.update({"Brake:":20, "phone: ":55555})

for keys, values in cluster_data.items():
    if keys =="speed:" and values>120:
        print("Overspeed warning")
    if keys=="fuel:" and values<40:
        print("low fuel warning")
        print(keys, values)

#delete
del cluster_data["fuel:"]
x= cluster_data.pop("door:")
print(x)
#length
print(len(cluster_data))
#keys
print(cluster_data.keys())
#values
print(cluster_data.values())
#both keys & values
print(cluster_data.items())
#only loop through keys
for values in cluster_data:
    print(values)
for val in cluster_data.values():
    print(val)