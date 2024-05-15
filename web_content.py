# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
#    a) листать параграфы текущей статьи;
#    b) перейти на одну из связанных страниц —
#       и снова выбор из двух пунктов:
#        - листать параграфы статьи;
#        - перейти на одну из внутренних статей.
#    c) выйти из программы.

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

def list_paragraphs(browser):
    for paragraph in browser.find_elements(By.TAG_NAME, "p"):
        print(paragraph.text)
        input()
#        time.sleep(3)

def choice_page(browser):

    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "mw-search-result-heading":
            page = element.find_element(By.TAG_NAME, "a")
            link = page.get_attribute("href")
            browser.get(link)
            time.sleep(10)
            break

def transfer_page(browser):
    pages = []

    try:
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "mw-search-result-heading":
                pages.append(element)

        page = random.choice(pages)
        link = page.find_element(By.TAG_NAME, "a").get_attribute("href")

        browser.get(link)
        time.sleep(10)

    except:
        print("Страниц не обнаружено")


print("Начинаем поиск информации")
user_input = input("Введите ваш запрос: ")

browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

assert "Википедия" in browser.title
time.sleep(5)
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(user_input)
search_box.send_keys(Keys.RETURN)

user_choice = input("Выберите действие: 1 - листать параграфы текущей статьи, 2 - перейти на одну из связанных страниц, 3 - выход\n")

if user_choice == "1":
    choice_page(browser)
    list_paragraphs(browser)
elif user_choice == "2":
    transfer_page(browser)
    select_again = input("Хотите продолжить поиск ? (да/нет) ")
    if select_again.lower() == "да":
        user_choice = input("Выберите действие: 1 - листать параграфы текущей статьи, 2 - перейти на одну из связанных страниц, 3 - выход\n")
        if user_choice == "1":
            list_paragraphs(browser)
        elif user_choice == "2":
            transfer_page(browser)
        else:
            browser.quit()
    else:
        browser.quit()
else:
    browser.quit()