import json
import os.path
import requests
import subprocess
from urllib.parse import urlparse

from analisys import analisys
from get_query import get_query


def browse(query):
    if not os.path.exists(f".\\results\\{query}.json"):
        print("Такого файла нет")
        while True:
            print("Произвести поиск в интернете? [y/n]")
            flag = input()
            if flag == "y":
                query, prompt = get_query()
                analisys(query, prompt)
                return
            elif flag == "n":
                return
            else:
                print(f"Неизвестная команда: {flag}")
    else:
        with open(f".\\results\\{query}.json", "r") as f:
            data = json.load(f)
        for i, key in enumerate(data.keys()):
            print(f'{i}: {key}')
    index = int(input("Выберите необходимый файл: "))
    if index not in range(len(data.keys())):
        print('Индекс вне границ')
        browse(query)
        return
    index_path = f".\\results\\{query}.json"
    file_path = download_file(index_path, index)

    subprocess.Popen(file_path, shell=True)


def download_file(path, index):
    with open(path) as f:
        data = json.load(f)
        url = list(data.values())[index]
        file_type = get_file_type_from_url(url)
        file_path = f".\\downloads\\{list(data.keys())[index]}{file_type}"
        if not os.path.exists(file_path):
            r = requests.get(url, stream=True)
            with open(file_path, "wb") as f:
                f.write(r.content)
    return file_path


def get_file_type_from_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    if ('.pdf' in path):
        return '.pdf'
    elif ('.ppt' in path):
        return '.ppt'
    elif ('.pptx' in path):
        return '.pptx'
    else:
        return ''

# subprocess.Popen("some_pdf", shell=True)
