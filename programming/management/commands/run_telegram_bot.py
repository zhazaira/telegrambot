from django.core.management.base import BaseCommand
import telebot
from programming.models import Programming

bot = telebot.TeleBot("6301458097:AAGXLQRv4dmFUH0V-CyjHTenX3dxYykAZms") 


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['products'])
def products(message):
    products = Programming.objects.all()
    for product in products:
        bot.send_message(message.chat.id, product.language)


@bot.message_handler(commands=['help'])
def help_command(message):
    commands = [
        "/start - Начать",
        "/products - Показать все языки",
        "/help - Помощь",
        "/add - Добавить новый язык"
        # Add more commands here
    ]
    help_text = "\n".join(commands)
    bot.send_message(message.chat.id, f"Available commands:\n\n{help_text}")

@bot.message_handler(commands=['add'])
def add_product(message):
    # Get the command arguments
    command_args = message.text.split()[1:]

    if len(command_args) != 2:
        bot.reply_to(message, "Неверный формат команды. Используйте: /add <language> <since>")
        return

    language= command_args[0]
    since = command_args[1]

    # Create a new product
    Programming.objects.create(language=language, since=since)
    bot.reply_to(message, f"Язык {language} сушествует с {since} года")

# ... The rest of your code ...

# The Django management command
class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")