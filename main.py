from browse import browse
from analisys import analisys
import json

from get_query import get_query

while True:
    command_select = input("Главное меню: \n"
                           "1 - анализ \n"
                           "2 - просмотр \n"
                           "3 - выход \n")
    print(command_select)
    match command_select:
        case "1":
            query, prompt = get_query()
            analisys(query, prompt)
        case "2":
            query = get_query()
            browse(query[0])

        case "3":
            break
        case _:
            print(f"Неизвестная команда: '{command_select}'")
