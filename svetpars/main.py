import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.divan.ru/category/svet"

driver.get(url)
time.sleep(5)

lamps = driver.find_elements(by=By.CLASS_NAME, value="WdR1o")

parsed_data = []

for lamp in lamps:
    try:
        name = lamp.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        price = lamp.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
        url = lamp.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
    except:
        print("Прозошла ошибка парсинга")
        continue


    parsed_data.append([name, price, url])

driver.quit()


with open("svet.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(['Название светильника', 'Цена', 'Ссылка на модель'])
    writer.writerows(parsed_data)
