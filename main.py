from search import general_search
from analysis import get_query
from view import view
import json

while True:
    command_select = input("Главное меню: \n"
                           "1 - анализ \n"
                           "2 - просмотр \n"
                           "3 - выход \n")
    print(command_select)
    match command_select:
        case "1":
            query, prompt = get_query()

            if query != "0":
                result = general_search(prompt)
                with open(f".\\results\\{query}.json", "w") as f:
                    json.dump(result, f)
        case "2":
            view()

        case "3":
            break
        case _:
            print(f"Неизвестная команда: '{command_select}'")