import json
import os.path
def browse(query):
    if not os.path.exists(f".\\results\\{query}.json"):
        print("Такого файла нет")
    else:
        with open(f".\\results\\{query}.json", "r") as f:
            data = json.load(f)
        for i, key in enumerate(data.keys()):
            print(f'{i + 1}: {key}')
        # for key, value in data.items():
        #     print(f"{key}: {value}")



