def get_query():
    query = "0"
    while True:
        request_select = input("Выбор запроса:\n"
                               "1 - поиск учебных пособий\n"
                               "2 - поиск конспектов лекций\n"
                               "3 - поиск учебной презентаций\n"
                               "0 - выход\n")
        match request_select:
            case "1":
                theme = input("Введите тему учебного пособия: ")
                query = 'filetype:pdf intext:"учебное пособие" ' + theme
                break
            case "2":
                theme = input("Введите тему необходимого конспекта: ")
                query = 'intext:"конспекты лекций" ' + theme
                break
            case "3":
                theme = input("Введите тему презентации: ")
                query = 'filetype:ppt intext:"лекция" ' + theme
                break
            case "0":
                break
            case _:
                print(f"Неизвестная команда: '{request_select}'")
    return query
