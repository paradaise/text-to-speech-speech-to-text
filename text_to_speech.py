import gtts

def convert_text_to_speech(bot,message):
    tts = gtts.gTTS(message.text, lang="ru")
    tts_path = f"text/{message.from_user.username}.wav"
    tts.save(tts_path)
    bot.send_message(message.chat.id, f"<i>{message.from_user.username}</i>,вот твое голосовое сообщение!🗣",parse_mode="html")
    bot.send_audio(message.chat.id, open(tts_path,'rb'))


