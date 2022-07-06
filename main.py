import logging
import os
from telebot import TeleBot
from common import str2mdown
from emoji import emojize

from db import subscriptions
from services import sports

BOT_TOKEN = "5417516229:AAH3PT7sICWcpea4Czn_-Q6ea93l5MMDQVg"

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Load environment variables
bot = TeleBot(BOT_TOKEN, parse_mode="MarkdownV2")

WELCOME_STRING = emojize(
    """Hi {name} :waving_hand:, welcome to UNISA Telegram Bot!
Here's a few things you can ask me:
- /help or /start to display this help message

*Subscription*
- /subscribe to enable notifications
- /remove or /unsubscribe to cancel from notifications

*Activities*
- /sport to randomly select an activity
"""
)


@bot.message_handler(commands=["start", "help"])
@bot.message_handler(func=lambda msg: msg.text.strip() in ["start", "help"])
def send_welcome(message):
    logging.info(f"Requested start or help from {message.from_user.id}")
    bot.send_message(
        message.chat.id,
        str2mdown(WELCOME_STRING.format(name=message.from_user.first_name)),
    )


@bot.message_handler(commands=["subscribe"])
@bot.message_handler(func=lambda msg: msg.text.strip() in ["subscribe"])
def handle_subscription(message):
    logging.info(f"Chat id {message.chat.id} requested to subscribe.")
    existing_sub = subscriptions.get_subscription(message.chat.id)

    if existing_sub is None:
        subscriptions.add_subscription(message.chat.id, message.from_user.first_name)
        msg = emojize("You are now subscribed! :thumbs_up:")
    else:
        msg = "You are already subscribed for notifications!"

    bot.send_message(message.chat.id, str2mdown(msg))


@bot.message_handler(commands=["remove", "unsubscribe"])
@bot.message_handler(func=lambda msg: msg.text.strip() in ["remove", "unsubscribe"])
def handle_unsubscribe(message):
    logging.info(f"Chat id {message.chat.id} requested to unsubscribe")
    if subscriptions.remove_subscription(message.chat.id):
        msg = (
            "Sorry to see you go! Remember, you can always re-subscribe with /subscribe"
        )
    else:
        msg = "You are not subscribed for notifications at the moment. If you wish to subscribe use /subscribe"

    bot.send_message(message.chat.id, str2mdown(msg))


@bot.message_handler(commands=["sport"])
@bot.message_handler(func=lambda msg: msg.text.strip() in ["sport"])
def handle_sport(message):

    bot.send_message(
        message.chat.id,
        str2mdown("What's the weather like today?"),
        reply_markup=sports.gen_markup_weather(),
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("weather_"))
def callback_sport(call):
    weather = call.data.split("_")[1]
    choice = sports.get_random_sport(weather)
    bot.answer_callback_query(call.id, show_alert=False)
    bot.send_message(call.message.chat.id, str2mdown(choice))


@bot.message_handler(content_types=["text"])
def text_message_handler(message):
    logging.info(
        f"Handling text message from user {message.from_user.id}. Content:\n{message.text}"
    )


logging.info("Starting Telegram bot!")
bot.polling()
