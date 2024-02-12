from search import general_search
from get_query import get_query
import json


def analisys(query, prompt):
    if query != "0":
        result = general_search(prompt)
        with open(f".\\results\\{query}.json", "w") as f:
            json.dump(result, f)
