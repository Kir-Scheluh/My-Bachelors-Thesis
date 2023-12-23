# Импорты для работы программы
from search_engines import Yahoo
from search_engines import Google
from search_engines import Ask
from search_engines import Startpage
from search_engines import Bing
from filter_search_results import filter_results
from data_visualization import horizontal_histogram


def general_search(query):
    if type(query) == Exception:
        return 0

    result = {'Yahoo': filter_results(search_with_yahoo(str(query))),
              'Google': filter_results(search_with_google(str(query))),
              'Ask': filter_results(search_with_ask(str(query))),
              'Startpage': filter_results(search_with_startpage(str(query))),
              'Bing': filter_results(search_with_bing(str(query)))}
    names = list(result.keys())
    data = []
    for i in result.values():
        data.append(len(i))

    print('Количество результатов:')
    horizontal_histogram(data, names)

    return result


def search_with_yahoo(query):
    engine = Yahoo()
    search_result = engine.search(str(query))
    output = search_result.links()

    return output


def search_with_google(query):
    engine = Google()
    search_result = engine.search(str(query))
    output = search_result.links()

    return output


def search_with_ask(query):
    engine = Ask()
    search_result = engine.search(str(query))
    output = search_result.links()

    return output


def search_with_startpage(query):
    engine = Startpage()
    search_result = engine.search(str(query))
    output = search_result.links()

    return output


def search_with_bing(query):
    engine = Bing()
    search_result = engine.search(str(query))
    output = search_result.links()

    return output
