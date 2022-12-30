import emoji
import io
from googletrans import Translator
t = Translator()
def menu():
    print(emoji.emojize(':one: for Portuguese', language='alias', variant='emoji_type'))
    print(emoji.emojize(':two: for English', language='alias', variant='emoji_type'))
    print(emoji.emojize(':three: for Spanish', language='alias', variant='emoji_type'))

menu()
language = 'pt'
print(emoji.emojize('Type :zero: for exit the program', language='alias', variant='emoji_type'))
option = int(input('Type a number the language you want to translate: '))

def translation():

    file_to_translate = open('put_here_the_text_to_translate.txt', 'r', encoding='utf-8')
    text = file_to_translate.read()
    file_to_translate.close()
    text_clean = text.strip()
    translated = t.translate(text_clean, dest=language, service_urls=['https://translate.google.com/'])
    print(emoji.emojize('Text translated: {}'.format(translated.text)))
    print(emoji.emojize('Thank you for using! :v:', language='alias', variant='emoji_type'))
    final_file = open('translated.txt', 'w')
    final_file.write(translated.text)
    final_file.close()
    exit()

while option != 0:
    if option == 1:
        language = 'pt'
        translation()
    elif option == 2:
        language = 'en'
        translation()
    elif option == 3:
        language = 'es'
        translation()
    else:
        print(emoji.emojize('Option invalid! :pensive: \n', language='alias', variant='emoji_type'))
        menu()
        option = int(input('Type a number the language you want to translate: '))

print(emoji.emojize('\nThank you for using! :v:', language='alias', variant='emoji_type'))
