import json
file_path = "C:\\Users\\nazvi\\Documents\\PP2-2024\\lab4\\json\\sample-data.json"

with open(file_path) as f:
    data = json.load(f)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for j in data['imdata']:
    l1PhysIf_data = j.get("l1PhysIf")  # Get the value associated with the 'l1PhysIf' key
    if l1PhysIf_data:  # Check if 'l1PhysIf' key exists and has a value
        attributes_data = l1PhysIf_data.get("attributes")  # Get the value associated with the 'attributes' key
        if attributes_data:  # Check if 'attributes' key exists and has a value
            print(attributes_data.get("dn"), attributes_data.get("descr"), attributes_data.get("speed"), attributes_data.get("mtu"))