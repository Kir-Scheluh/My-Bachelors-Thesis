from browse import browse
from analisis import analysis
from User import User

from get_query import get_query


def authorization():
    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        user = User(login, password)
        if user.is_authorized:
            print("Успешно!")
            while True:
                main_menu(user)
        else:
            print("Неверные данные для входа!")


def main_menu(user):
    while True:
        command_select = input("Главное меню: \n"
                               "1 - анализ \n"
                               "2 - просмотр \n"
                               "3 - панель администратора \n"
                               "4 - выход \n")
        print(command_select)
        match command_select:
            case "1":
                query, prompt = get_query()
                analysis(query, prompt)
            case "2":
                query = get_query()
                browse(query[0])
            case "3":
                if not user.is_admin:
                    print("У вас недостаточно прав для этой секции")
                    break
                admin_command = input("Панель администратора:\n"
                                      "1 - создать учетную запись\n"
                                      "2 - удалить учётную запись\n"
                                      "3 - выход\n")
                print(admin_command)
                match admin_command:
                    case "1":
                        user.create_user()
                    case "2":
                        user.delete_user()
                    case "3":
                        break
                    case _:
                        print(f"Неизвестная команда: '{command_select}'")
            case "4":
                authorization()
                break
            case _:
                print(f"Неизвестная команда: '{command_select}'")


authorization()
