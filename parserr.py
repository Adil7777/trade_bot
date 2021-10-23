from bs4 import BeautifulSoup
import requests


class Trade:
    def __init__(self):
        self.url = 'https://www.google.com/search?q=apple+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8&oq=apple+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8&aqs=chrome..69i57j0i512l9.226631j1j7&sourceid=chrome&ie=UTF-8'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

    def parse_(self):
        page = requests.get(self.url, self.headers)
        content = BeautifulSoup(page.content, 'html.parser')
        a = content.findAll('div', {'class': 'BNeawe iBp4i AP7Wnd'})
        return a[1].text
