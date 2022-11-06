from turtle import down
import telebot
import credentials
from io import BytesIO
import requests
from PIL import Image
from os import path, rename
import base64
import cv2
from pyzbar.pyzbar import decode
from datetime import datetime

#Variables

Path = credentials.Path
voucher_number = 0

bot = telebot.TeleBot(credentials.bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello World, use /help to learn more commands")

@bot.message_handler(commands=['version'])
def version(message):
    bot.reply_to(message, "1.0")


@bot.message_handler(content_types=['photo'])
def add(message):
    now = datetime.now()
    current_time = now.strftime("%d%b%H-%M-%S")
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    file = requests.get(f'https://api.telegram.org/file/bot{credentials.bot_token}/{fileID}'.format(credentials.bot_token, file_info.file_path)) 
    downloaded_file = bot.download_file(file_info.file_path)
    with open(path.join(Path , f"{current_time}.jpg"), 'wb') as new_file:
        new_file.write(downloaded_file) 
    bot.reply_to(message, f"Added as {current_time}.jpg")
    

    
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 
    """
    Commands that you can use:
    /start    ->    Replies with Hello world
    /version  ->    Shows the current released version
    /help     ->    Thats how you got here
    """         
                 )

bot.infinity_polling()