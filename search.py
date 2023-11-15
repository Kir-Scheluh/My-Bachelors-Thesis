#Импорты для обработки ошибок
import socket
import requests
import ssl
import urllib3

from search_engines import Yahoo
from search_engines import Google
from search_engines import Ask
from filter_search_results import filter_results
from data_visualization import horizontal_histogram
from get_title import get_html_title


def general_search(url):
    try:
        query = get_html_title(url)
    except requests.exceptions.Timeout:
        print("Ошибка: превышено время ожидания")
        return requests.exceptions.Timeout
    except requests.exceptions.MissingSchema:
        print("Неверный формат URL")
        return requests.exceptions.MissingSchema
    except AttributeError:
        print("Ошибка при считывании заголовка страницы")
        return AttributeError
    except ssl.SSLError:
        print("Ошибка: sslv3 alert handshake failure")
        return ssl.SSLError
    except socket.gaierror:
        print("Ошибка: socket.gaierror: [Errno 11001] getaddrinfo failed")
        return socket.gaierror
    except urllib3.exceptions.NameResolutionError:
        print("Ошибка: urllib3.exceptions.NameResolutionError")
        return urllib3.exceptions.NameResolutionError
    print(f'Запрос: {query}')

    result = {'Yahoo': filter_results(search_with_yahoo(str(query))),
              'Google': filter_results(search_with_google(str(query))),
              'Ask': filter_results(search_with_Ask(str(query)))}
    names = list(result.keys())
    data = []
    for i in result.values():
        data.append(len(i["hosts"]))

    print('Количество результатов:')
    horizontal_histogram(data, names)

    return result


def search_with_yahoo(query):
    engine = Yahoo()
    search_result = engine.search(str(query))
    output = {'hosts': search_result.hosts(), 'titles': search_result.titles(), 'links': search_result.links()}

    return output


def search_with_google(query):
    engine = Google()
    search_result = engine.search(str(query))
    output = {'hosts': search_result.hosts(), 'titles': search_result.titles(), 'links': search_result.links()}

    return output


def search_with_Ask(query):
    engine = Ask()
    search_result = engine.search(str(query))
    output = {'hosts': search_result.hosts(), 'titles': search_result.titles(), 'links': search_result.links()}

    return output
