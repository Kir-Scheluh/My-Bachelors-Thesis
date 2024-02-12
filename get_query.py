def get_query():
    query = "0"
    theme = ""
    while True:
        request_select = input("Выбор запроса:\n"
                               "1 - учебные пособия\n"
                               "2 - конспекты лекций\n"
                               "3 - учебные презентации\n"
                               "0 - выход\n")
        match request_select:
            case "1":
                theme = input("Введите тему учебного пособия: ")
                query = 'filetype:pdf intext:"учебное пособие" ' + theme
                theme += ' [учебные пособия]'
                break
            case "2":
                theme = input("Введите тему необходимого конспекта: ")
                query = 'intext:"конспекты лекций" ' + theme
                theme += ' [конспекты]'
                break
            case "3":
                theme = input("Введите тему презентации: ")
                query = 'filetype:ppt intext:"лекция" ' + theme
                theme += ' [презентации]'
                break
            case "0":
                break
            case _:
                print(f"Неизвестная команда: '{request_select}'")
    return theme, query
