import nltk
from textblob import TextBlob
from googletrans import Translator, constants
from pprint import pprint

string = str(input('Введите строку для перевода и эмоциональной оценки: '))
translator = Translator()
translation = translator.translate(string)
print(translation.text)
analysis = TextBlob(translation.text).sentiment
print('----------------------------------')
print('Эмоциональная оценка : ')
print(analysis)
