import telebot
import credentials


bot = telebot.TeleBot(credentials.bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello World, use /help to learn more commands")

@bot.message_handler(commands=['version'])
def version(message):
    bot.reply_to(message, "1.0")
    
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