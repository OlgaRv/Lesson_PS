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

url = "https://tomsk.hh.ru/vacancies/programmist"

driver.get(url)
time.sleep(5)

vacancies = driver.find_elements(by=By.CLASS_NAME, value="vacancy-card--H8LvOiOGPll0jZvYpxIF")

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except:
        print("Прозошла ошибка парсинга")
        continue


    parsed_data.append([title, company, salary, link])

driver.quit()


with open("hh.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(['Название вакансии', 'Компания', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)
