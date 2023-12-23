from search import general_search
from get_title import get_html_title

while True:
    current_command = input("Главное меню: \n"
                            "1 - анализ \n"
                            "2 - просмотр \n"
                            "3 - выход \n")
    print(current_command)
    if current_command == "1":
        url = input("Введите url для запроса: ")
        query = get_html_title(url)
        general_search(query)
    elif current_command == "2":
        pass
        # Функция для просмотра
    elif current_command == "3":
        break
    else:
        print(f"Неизвестная команда: '{current_command}'")
