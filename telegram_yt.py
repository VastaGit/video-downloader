import requests
import telebot
from pytube import YouTube
from telebot import types
import asyncio
from key import token

bot = telebot.TeleBot("5113529227:" + token, parse_mode = None)

async def Downloader(url):
    yt = YouTube(url)
    yt.streams.get_by_itag(22)
    stream = yt.streams.get_by_itag(22)
    stream.download()
    print("waiting")
    await asyncio.sleep(180)

@bot.message_handler(commands=['start'])
def default(message):
    bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}. Ready to download some videos from Youtube? Just send me the link")

@bot.message_handler(func=lambda m: True)
def url_accepting(message):
    yt = YouTube(message.text)
    asyncio.run(Downloader(message.text))
    bot.send_message(message.chat.id, "Downloading finished")
    video=open(f'{yt.title}.mp4', 'rb')
    bot.send_video(message.chat.id, video, timeout=500)


    # await foo()
    # await print_numberds()


bot.polling()

    # greeting_markup = types.ReplyKeyboardMarkup(row_width=2)
    # itembtn1 = types.KeyboardButton('✅Subscribe')
    # itembtn2 = types.KeyboardButton('☑️Unsubscribe')    
    # greeting_markup.add(itembtn1, itembtn2)
    # bot.send_message(message.chat.id, "want to track?", reply_markup = greeting_markup)