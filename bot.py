import os

from dotenv import load_dotenv
from javascript import require

load_dotenv()


mineflayer = require('mineflayer')
bot_username = 'MineAI'


def InitialiseBot():
    return Bot()


class Bot:
    def __init__(self):
        print("Bot created")
        self.bot = mineflayer.createBot({
            'host': os.getenv('IP'),
            'port': 25565,
            'username': bot_username,
            'hideErrors': False,
        })
    
    def connect_bot(self):
        print('Bot logged in')
        self.bot.chat(f'I spawned at {self.bot.entity.position}')
    
    def disconnect_bot(self):
        self.bot.quit()
        print('Bot disconnected')
    
    #
    # @On('playerJoin')
    # def end(self, player):
    #     bot.chat(f"Someone joined! It's {player.username}")
    #
    # @On('playerLeft')
