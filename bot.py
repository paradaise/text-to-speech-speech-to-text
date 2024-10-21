import telebot
from api_key import TOKEN
from text_to_speech import convert_text_to_speech
from speech_to_text import speech_to_text

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет,<b>{message.from_user.username}</b>🤤\nЕсли отправишь мне ГС я переведу его в текст!😱\nА если отправишь мне текст я переведу его в ГС!😎",parse_mode="html")
    bot.send_message(message.chat.id, f"И да, ты можешь пересылать и текст и аудио.",parse_mode="html")

@bot.message_handler(content_types=['text','voice'])
def handle_message(message):
    if message.content_type == 'text':
        convert_text_to_speech(bot,message)
    if message.content_type == 'voice':
        speech_to_text(bot,message)


bot.polling(non_stop=True)


#добавить в бота:
    #сообщение что бот работает только с текстом и голосом если пришло геолокация,стикер
    #переводить в текст песни,видео,кружки
    #добавить автоопределения text to speech, если пришло сообщение на английском подставлять в параметр lang="eu" 
    #добавить выбор голоса для text-to-speech(мужчина,женщина)