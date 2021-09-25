import json
import random
import requests
from telegram_bot.settings import BOT_URL


def get_chat_id(data):
    try:
        chat_id = data['callback_query']['from']['id']
    except:
        chat_id = data['message']['chat']['id']

    return chat_id


def get_message(data):
    try:
        message_text = data['callback_query']['data']
    except:
        message_text = data['message']['text']

    return message_text


def get_user(data):
    try:
        username = data['callback_query']['from']['first_name']
    except:
        username = None

    return username


def get_jokes(text):
    text = text.lower()
    jokes = {
        'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                   """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
        'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                   """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
        'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                   """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
    }
    result_message = {}
    if 'stupid' in text:
        result_message['text'] = random.choice(jokes['stupid'])

    elif 'fat' in text:
        result_message['text'] = random.choice(jokes['fat'])

    elif 'dumb' in text:
        result_message['text'] = random.choice(jokes['dumb'])

    elif 'start' in text:
        result_message['text'] = "Hi there! I'm the Joke bot.\nLet's have some fun. Please select one of the options to hear jokes."

    elif text in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes, please select one of the below options."

    return result_message['text']


def send_response(message, chat_id):
    headers = {"Content-Type": "application/json"}
    data = {
        "chat_id": chat_id,
        "text": message,
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "Stupid", "callback_data": "stupid", }],
                [{"text": "Fat", "callback_data": "fat", }],
                [{"text": "Dumb", "callback_data": "dumb", }]
            ]
        }
    }
    data = json.dumps(data)
    response = requests.post(
        f"{BOT_URL}/sendMessage", headers=headers, data=data
    )
