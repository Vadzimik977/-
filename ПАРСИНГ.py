# ДО QUIT ВЕРНЫЙ МЕТОД ПАРСИНГА

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
# Инициализация драйвера Selenium
driver = webdriver.Chrome()
# Открытие страницы
url = "https://combot.org/top/telegram/groups?lng=en&page=1"
driver.get(url)
def scroll_to_end(scroll_count):
    for _ in range(scroll_count):
        prev_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'chats')))
        sleep(2)
        current_height = driver.execute_script("return document.body.scrollHeight")
        if current_height == prev_height:
            break

# Прокручиваем страницу до конца и ожидаем загрузку данных
scroll_count = 3000  # Можно настроить количество спусков
scroll_to_end(scroll_count)

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'chats')))

soup = BeautifulSoup(driver.page_source, 'html.parser')
chats_div = soup.find('div', {'id': 'chats'})
card_titles = chats_div.find_all('span', {'class': 'card-title'})
card_usernames = chats_div.find_all('span', {'class': 'card-username'})

# Создаем пустой список для хранения данных
data_list = []

# Добавляем данные в список
for title, username in zip(card_titles, card_usernames):
    title_text = title.get_text()
    username_text = " ".join(user.get_text() for user in username)
    data_list.append(f"{title_text} - {username_text}")

# scroll_to_bottom()
# Записываем данные в файл
with open("parsed_data.html", "w", encoding="utf-8") as file:
    for data in data_list:
        file.write(data + "\n")

# Закрытие браузера
driver.quit()