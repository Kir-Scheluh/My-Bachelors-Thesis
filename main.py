while True:
    current_command = input("Главное меню: \n"
                            "1 - анализ \n"
                            "2 - просмотр \n"
                            "3 - выход \n")
    print(current_command)
    if current_command == "1":
        pass
        # Функция для анализа
    elif current_command == "2":
        pass
        # Функция для просмотра
    elif current_command == "3":
        break
    else:
        print("Неизвестная команда")
