import requests
from bs4 import BeautifulSoup

def get_html_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.title.string

print(get_html_title("https://login.mirea.ru/login/?next=/oauth2/v1/authorize/%3Fresponse_type%3Dcode%26client_id%3DdnOh7sdtPxfyxzbxcMRLksWlCCE3WsgTfRY6AWKh%26redirect_uri%3Dhttps%3A%2F%2Fonline-edu.mirea.ru%2Flogin%2F%26scope%3Dbasic%2Bstudent"))