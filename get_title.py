import re

def delete_url(original_string):

    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    match = url_pattern.search(original_string)

    if match:
        # если найдено совпадение, удалить URL адрес и все последующие символы
        original_string = original_string.split(match.group())[0]

    return (original_string)
