from bs4 import BeautifulSoup
import requests

def get_englishword():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "word": english_word,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_word()
        word = word_dict.get("english_word")
        word_difination = word_dict.get("word_definition")

        print(f"Значение слова - {word_difination}")
        user = input("Что это за слово? ")
        if user == word:
            print("Всё верно!")
        else:
            print(f"Ответ неверный, было загадано слово - {word}")

        play_again = input("Хотите сыграть еще раз? (y/n) ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()
