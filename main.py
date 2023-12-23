from search import general_search
from get_title import get_html_title

while True:
    current_command = input("Главное меню: \n"
                            "1 - анализ \n"
                            "2 - просмотр \n"
                            "3 - выход \n")
    print(current_command)
    match current_command:
        case "1":
            url = input("Введите url для запроса: ")
            query = get_html_title(url)
            general_search(query)
        case "2":
            pass
            # Функция для просмотра
        case "3":
            break
        case _:
            print(f"Неизвестная команда: '{current_command}'")
