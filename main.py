from search import general_search
from analysis import get_query

while True:
    command_select = input("Главное меню: \n"
                           "1 - анализ \n"
                           "2 - просмотр \n"
                           "3 - выход \n")
    print(command_select)
    match command_select:
        case "1":
            query = get_query()

            if query != "0":
                result = general_search(query)

        case "2":
            pass
            # Функция для просмотра
        case "3":
            break
        case _:
            print(f"Неизвестная команда: '{command_select}'")