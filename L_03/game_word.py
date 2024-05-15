from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find("div", id="random_word").text.strip()
        target_word = translate_word(english_word)
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        target_definition = translate_word(word_definition)
        return {
            "word": target_word,
            "word_definition": target_definition
        }
    except:
        print("Произошла ошибка")

def translate_word(word):
    translator = Translator()
    translation = translator.translate(word, dest="ru")
    return translation.text

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_word()
        word = word_dict.get("word")
        word_difination = word_dict.get("word_definition")

        print(f"Значение слова - {word_difination}")
        user = input("Что это за слово? ")
        if user == word:
            print("Всё верно!")
        else:
            print(f"Ответ неверный, было загадано слово - {word}")

        play_again = input("Хотите сыграть еще раз? (да/нет) ")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break

word_game()



