from turtle import down
import telebot
import credentials
from io import BytesIO
import requests
from PIL import Image
from os import path, rename,listdir
import base64
import cv2
from pyzbar.pyzbar import decode
from datetime import datetime

#Variables

Path = credentials.Path

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
    
@bot.message_handler(commands=['list'])
def list(message):
    items = 0
    list = listdir(Path)
    ans = ''
    for item in list:
        ans += item + '\n'
        items += 1
    if items == 0:
        ans = "There are no vouchers present"
    else: ans += f"\nIn total there are {items} vouchers"
    bot.reply_to(message, ans)
    
    
@bot.message_handler(commands=['give'])
def give(message):
    name_file = listdir(Path)
    if len(name_file) ==  0:
            bot.reply_to(message, text='There are no vouchers present')
    else:
        name = name_file[0] #shows the first file that appears on the folder
        test = open(Path + str(name))
        bot.send_photo(message.chat.id,photo=open(Path + str(name), 'rb') , caption = 'Returned voucher', reply_markup=keyboard)
    
button_foo = telebot.types.InlineKeyboardButton('Delete this voucher', callback_data='foo')
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.add(button_foo)



    
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 
    """
    Commands that you can use:
    /start    ->    Replies with Hello world
    /version  ->    Shows the current released version
    /help     ->    Thats how you got here
    /list     ->    Returns a list of files and in the end the total number of them
    """         
                 )

bot.infinity_polling()