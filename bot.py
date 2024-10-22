import telebot
from api_key import TOKEN
from text_to_speech import convert_text_to_speech
from speech_to_text import speech_to_text

bot = telebot.TeleBot(TOKEN)    

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет,<b>{message.from_user.username}</b>🤤\nЕсли отправишь мне ГС я переведу его в текст!😱\nА если отправишь мне текст я переведу его в ГС!😎",parse_mode="html")
    bot.send_message(message.chat.id, f"И да, ты можешь пересылать как текст, так и голосовое сообщение.",parse_mode="html")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEJYDZnF7KdbNKdQQ4UyWmnNXBcQ-ShfwACHj8AAgnoEEgB8nsNObsWRjYE')

@bot.message_handler(content_types=['text','voice'])
def handle_message(message):
    if message.content_type == 'text':
        convert_text_to_speech(bot,message)
    if message.content_type == 'voice':
        speech_to_text(bot,message)

@bot.message_handler(content_types = ['photo', 'sticker', 'location','document'])
def handle_error(message):
    bot.send_message(message.chat.id, f"Извини, бот не работает с <i>{message.content_type}!</i> ",parse_mode="html")

@bot.message_handler(content_types = ['video', 'video_note', 'audio'])
def handle_error(message):
    bot.send_message(message.chat.id, f"Перевод <i>{message.content_type}</i> в текст пока находится в разработке:((",parse_mode="html")


bot.polling(non_stop=True)



#добавить в бота:
    #переводить в текст песни,видео,кружки
    #добавить автоопределения TTS, если пришло сообщение на английском подставлять в параметр lang="eu" 
    #добавить выбор голоса для text-to-speech(мужчина,женщина)