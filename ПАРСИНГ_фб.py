from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# Ссылка для логина
login_url = 'https://www.facebook.com/login/'

# учетные данные для авторизации
username = 
password = 

# Загружаем страницу входа
driver.get(login_url)


username_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')

username_input.send_keys(username)
password_input.send_keys(password)

# Нажимаем клавишу Enter
password_input.send_keys(Keys.RETURN)

# Ждем, чтобы страница прогрузилась (может потребоваться регулировать время ожидания)
time.sleep(5)

# Адрес страницы
url = 'https://www.facebook.com/groups/277415100803816/members?locale=ru_RU'

# Загружаем страницу группы
driver.get(url)

# Ждем, чтобы страница прогрузилась
time.sleep(5)

# Прокрутки
scroll_count = 10000

for _ in range(scroll_count):
    # Прокручиваем страницу вниз
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # Подождем немного после каждой прокрутки

# Получаем и сохраняем ссылки на пользователей
user_links = []
elements = driver.find_elements(By.TAG_NAME, 'a')
for element in elements:
    href = element.get_attribute('href')
    if href and '/user/' in href:
        user_links.append(href)

# Закрываем браузер
driver.quit()

# Сохраняем ссылки на пользователей в файл
with open('user_links.txt', 'w') as file:
    for user_link in user_links:
        file.write(user_link + '\n')

print('Ссылки на пользователей сохранены в файл user_links.txt')
