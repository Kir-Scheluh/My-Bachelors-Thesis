from browse import browse
from analisys import analisys
from User import User

from get_query import get_query

while True:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    user = User(login, password)
    if user.is_authorized:
        print("Успешно!")
        break
    else:
        print("Неверные данные для входа")

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
