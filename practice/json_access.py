import json
test_data={
    "TC01":{"Speed": 120,
            "Fuel": 80,
            "Ign":"OFF"},
    "TC02":{"Speed": 80,
            "Fuel": 50,
            "Ign": "ON"}
}
with open ("test_data.json","w") as f:
    json.dump(test_data, f, indent=4)
with open ("test_data.json", "r") as f:
    data=json.load(f)
    for keys, values in data.items():
        print(f"Key is -> {keys}")  #print all keys
        print(f"Value of key ->{values}") #print values
    for key in data.keys():
        print(f"Key Name-> {key}")
    for value in data.values():
        print(f"Value Name-> {value}")
        #print only inner value
        print(value["Speed"])
    #Raw Keys and Value using list
    value_list= list(data.values())
    key_list= list(data.keys())
    print(f"value list->{value_list}\nkey list->{key_list}")
    #get a specific value using key name
    single_value=data["TC01"]
    print(f"Single value->{single_value}")
