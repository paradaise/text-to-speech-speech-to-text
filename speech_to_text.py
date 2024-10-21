import speech_recognition as sr
import ffmpeg
import os


def get_voice_file(bot, message):
    file_info = bot.get_file(message.voice.file_id) # dict с инфой по файлу отправленному юзером
    downloaded_file = bot.download_file(file_info.file_path) #бинаринк аудио
    
    ogg_path = f'voice/{message.from_user.username}.ogg'
    with open(ogg_path, 'wb') as ogg_file:
        ogg_file.write(downloaded_file)
    
    return ogg_path

def convert_ogg_to_wav(ogg_path):
    wav_path = ogg_path.replace('.ogg', '.wav')
    if os.path.exists(wav_path):
        os.remove(wav_path)  # Удаляем файл, если он существует
    ffmpeg.input(ogg_path).output(wav_path).run()
    return wav_path

def wav_to_text(wav_path):
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='ru-RU')
    return text


def speech_to_text(bot,message):
    ogg_path = get_voice_file(bot, message)
    wav_path = convert_ogg_to_wav(ogg_path)
    recognize_text = wav_to_text(wav_path)
    bot.send_message(message.chat.id,f'<i><b>Вот что мне удалось услышать🦻🏼:</b></i>\n {recognize_text}', parse_mode="html")