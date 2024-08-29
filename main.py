import requests
from bs4 import BeautifulSoup

# Определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# URL страницы со статьями
URL = 'https://habr.com/ru/articles/'

# Загружаем страницу
response = requests.get(URL)
response.raise_for_status()

# Парсим HTML страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем все элементы, содержащие статьи
articles = soup.find_all('article')

# Перебираем все статьи
for article in articles:
    # Ищем превью статьи
    preview = article.find('div', class_='tm-article-snippet')
    if preview:
        preview_text = preview.text.lower()

        # Проверяем, содержит ли превью какое-либо из ключевых слов
        if any(keyword in preview_text for keyword in KEYWORDS):
            # Извлекаем дату, заголовок и ссылку на статью
            date = article.find('time')['datetime']
            title = article.find('a', class_='tm-article-snippet__title-link').text
            link = article.find('a', class_='tm-article-snippet__title-link')['href']
            full_link = f'https://habr.com{link}'

            # Выводим результат
            print(f"{date} – {title} – {full_link}")
