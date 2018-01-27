from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os 
import docker

def docker_show_image():
    client = docker.client.from_env()
    images = client.images.list()
    return '\n'.join([str(image) for image in images])

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='telegram_bot/bot.log'
                    )

def greet_user(bot, update):
    text = 'эй'
    print(text)
    update.message.reply_text(text)

def image_show(bot, update):
    user_text = update.message.text
    #print(user_text)
    docker_image_result = docker_show_image()
    update.message.reply_text(docker_image_result)

def main():
    # logging.basicConfig(level=logging.DEBUG)
    updater = Updater("510202673:AAEva8TduvxqT0JFQGCql_4n18ICBqyNok4")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("images", image_show))
    updater.start_polling()
    updater.idle()

main()