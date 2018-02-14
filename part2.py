import json

info_about_me = {
    "name": "Colby",
    "has_a_dog": True
}
with open("info.json", "w") as f:
    json.dump(info_about_me, f)

