import json
import pathlib
import config


with open("config.json", "r") as f:
    config = json.load(f)
print(config['email_Id'])