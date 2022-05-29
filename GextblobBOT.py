import nltk
import telebot
from textblob import TextBlob
from nltk.tokenize import PunktSentenceTokenizer
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import WordList
from textblob import Word
from googletrans import Translator, constants
from pprint import pprint

token = '5480699275:AAGv9QZXnyLafpiWehCkepcDNwC7W3wL46A'
bot = telebot.TeleBot('%s' % token)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    blob = TextBlob(message.text, analyzer=NaiveBayesAnalyzer())
    translator = Translator()
    translation = translator.translate(message.text)
    analysis = TextBlob(translation.text).sentiment
    bot.send_message(message.from_user.id,
                     'Список предложений:\n' +
                     '\n'.join(s.string for s in blob.sentences))
    #оценка
    bot.send_message(message.from_user.id, 
                    "эмоциональная оценка: " + str(analysis))
    # Токенизация
    bot.send_message(message.from_user.id,
                     'Токенизация:\n' + ', '.join(blob.words))
    # Удаление стоп-слов
    stopwords = ['a', 'able', 'about', 'above', 'abst',
                 'accordance', 'according', 'the']
    words = [word.lower() for word in blob.words
             if not word.isdigit() and word.lower() not in stopwords]
    bot.send_message(message.from_user.id,
                     'Удаление стоп слов:\n' + ', '.join(words))
    #
    bot.send_message(message.from_user.id,
                     'Лемитизация:\n' + ', '.join(WordList(words).lemmatize()))

    if blob.sentiment[0] == 'pos':
        bot.send_message(message.from_user.id, '\U0001F63A')
    else:
        bot.send_message(message.from_user.id, '\U0001F63F')
    word = Word('theyr')
    print(word.spellcheck())

bot.polling(none_stop=True, interval=0)
