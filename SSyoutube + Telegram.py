import requests
import telebot
from telebot import types
from selenium import webdriver
import time
from key import token

bot = telebot.TeleBot("5113529227:" + token , parse_mode = None)

def ssyoutube(url):

    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    chrome_browser = webdriver.Chrome('./chromedriver', options=op)
    chrome_browser.get('https://en.savefrom.net/19-ssyoutube-51.html')

    assert 'ssYoutube - Download a YouTube Video via ssYouTube.com' in chrome_browser.title

    button = chrome_browser.find_elements_by_id('sf_submit')
    url_input = chrome_browser.find_elements_by_id('sf_url')
    url_input[0].send_keys(url)
    button[0].click()
    time.sleep(5)
    return chrome_browser.find_element_by_class_name('link-download').get_attribute('href')

@bot.message_handler(commands=['start'])
def default(message):
    bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}. Ready to download some videos from Youtube? Just send me the link")

@bot.message_handler(func=lambda m: True)
def url_accepting(message):
    link = ssyoutube(message.text)
    bot.send_message(message.chat.id, link)

bot.polling()
