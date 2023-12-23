# Импорты для обработки ошибок
import socket
import ssl
import urllib3

import requests
from bs4 import BeautifulSoup


def get_html_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.title.string.rstrip()
    except requests.exceptions.Timeout:
        print("Ошибка: превышено время ожидания")
        return requests.exceptions.Timeout
    except requests.exceptions.MissingSchema:
        print("Неверный формат URL")
        return requests.exceptions.MissingSchema
    except AttributeError:
        print("Ошибка при считывании заголовка страницы")
        return AttributeError
    except ssl.SSLCertVerificationError:
        print("Ошибка: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired")
        return ssl.SSLCertVerificationError
    except ssl.SSLError:
        print("Ошибка: sslv3 alert handshake failure")
        return ssl.SSLError
    except socket.gaierror:
        print("Ошибка: socket.gaierror: [Errno 11001] getaddrinfo failed")
        return socket.gaierror
    except urllib3.exceptions.NameResolutionError:
        print("Ошибка: urllib3.exceptions.NameResolutionError")
        return urllib3.exceptions.NameResolutionError
