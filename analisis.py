from search import general_search
import json
from file_encryption import file_encrypt, load_key


def analysis(query, prompt):
    if query != "0":
        key = load_key()
        result = general_search(prompt)
        file_name = f".\\results\\{query}.json"
        with open(file_name, "w") as f:
            json.dump(result, f)
        file_encrypt(file_name, key)
