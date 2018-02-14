import json

with open("info.json", "r") as f:
    info = json.load(f)

if info["has_a_dog"]:
    print("{} has a dog".format(info["name"]))
else:
    print("{} does not have a dog".format(info["name"]))

    
