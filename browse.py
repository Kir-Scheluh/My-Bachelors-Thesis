import json
import os.path
import requests
import subprocess
from urllib.parse import urlparse

from analisis import analysis
from get_query import get_query
from file_encryption import file_encrypt, file_decrypt, load_key


def browse(query):
    key = load_key()
    file_name = f"results/{query}.json"
    if not os.path.exists(file_name):
        print("Такого файла нет")
        while True:
            print("Произвести поиск в интернете? [y/n]")
            flag = input()
            if flag == "y":
                query, prompt = get_query()
                analysis(query, prompt)
                return
            elif flag == "n":
                return
            else:
                print(f"Неизвестная команда: {flag}")
    else:
        file_decrypt(file_name, key)
        with open(file_name, "r") as f:
            data = json.load(f)
        file_encrypt(file_name, key)
        for i, key in enumerate(data.keys()):
            print(f'{i}: {key}')
    index = int(input("Выберите необходимый файл: "))
    if index not in range(len(data.keys())):
        print('Индекс вне границ')
        browse(query)
        return
    file_path = download_file(file_name, index)
    subprocess.Popen(file_path, shell=True)


def download_file(path, index):
    key = load_key()
    file_decrypt(path, key)
    with open(path) as f:
        data = json.load(f)
        url = list(data.values())[index]
        file_type = get_file_type_from_url(url)
        file_path = f".\\downloads\\{list(data.keys())[index]}{file_type}"
        if not os.path.exists(file_path):
            r = requests.get(url, stream=True)
            with open(file_path, "wb") as f1:
                f1.write(r.content)
            file_encrypt(file_path, key)
    file_encrypt(path, key)
    return file_path


def get_file_type_from_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    if '.pdf' in path:
        return '.pdf'
    elif '.ppt' in path:
        return '.ppt'
    elif '.pptx' in path:
        return '.pptx'
    else:
        return ''
