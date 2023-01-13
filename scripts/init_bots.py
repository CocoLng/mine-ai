import os
from time import sleep

from dotenv import load_dotenv
from javascript import require

load_dotenv()

mineflayer = require("mineflayer")
bot_username = "MineAI"


def createBot(name_bot):
    return mineflayer.createBot(
        {
            "host": os.getenv("IP"),
            "port": 25565,
            "username": name_bot,
            "hideErrors": False,
        }
    )


def multiplesBots(nb, name_bot, list_bot=None):
    if not list_bot:
        list_bot = []
    [
        list_bot.append(createBot(f"{name_bot}_{nb}"))
        for nb in range(1, nb)
        if sleep(5) is None
    ]
    return list_bot
