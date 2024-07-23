import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Firefox
driver = webdriver.Firefox()
url = "https://www.divan.ru/category/svet"

# Открытие URL
driver.get(url)

# Ожидание загрузки элементов на странице
wait = WebDriverWait(driver, 10)
fixtures = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'LlPhw')))
print(len(fixtures))

parsed_data = []

# Парсинг данных
for fixture in fixtures:
    try:
        name = fixture.find_element(By.CSS_SELECTOR, 'div.wYUX2 span').text
        price = fixture.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        link = fixture.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except Exception as e:
        print(f'Произошла ошибка при парсинге: {e}')
        continue

    parsed_data.append([name, price, link])

# Закрытие драйвера
driver.quit()

# Запись данных в CSV файл
with open('divan_fixtures.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)
