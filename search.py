# Импорты для работы программы
import re
from search_engines import Yahoo
from search_engines import Google
from search_engines import Ask
from search_engines import Startpage
from search_engines import Bing
from data_visualization import horizontal_histogram


def general_search(query):
    result = {'Yahoo': search_with(str(query), Yahoo),
              'Google': search_with(str(query), Google),
              'Ask': search_with(str(query), Ask),
              'Startpage': search_with(str(query), Startpage),
              'Bing': search_with(str(query), Bing)}
    names = list(result.keys())
    data = []
    for i in result.values():
        data.append(len(i))

    print('Количество результатов:')
    horizontal_histogram(data, names)

    merged_dict = {}
    for sub_dict in result.values():
        merged_dict.update(sub_dict)
    merged_dict = {key: value for key, value in merged_dict.items() if
                     list(merged_dict.values()).count(value) == 1}



    return merged_dict


def search_with(query, engine):
    engine = engine()
    search_result = engine.search(str(query))
    links = search_result.links()
    titles = search_result.titles()
    titles = [clear_url(title) for title in titles]
    output = dict(zip(titles, links))

    return output


def clear_url(original_string):
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    match = url_pattern.search(original_string)

    if match:
        # если найдено совпадение, удалить URL адрес и все последующие символы
        original_string = original_string.split(match.group())[0]

    return original_string
