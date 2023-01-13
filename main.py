####################################################
# cd .\server\
# java -jar .\spigot-1.8.8-R0.1-SNAPSHOT-latest.jar
####################################################

from javascript import require, On
from time import sleep
from scripts.init_bots import createBot, multiplesBots

bots = multiplesBots(5, "MineAI")
print(len(bots))

# mineflayer = require('mineflayer')
# pathfinder = require('mineflayer-pathfinder')
#
# RANGE_GOAL = 1
# BOT_USERNAME = 'MineAI'
#
# bot = mineflayer.createBot({
#     'host': '127.0.0.1',
#     'port': 25565,
#     'username': BOT_USERNAME
# })
#
# bot.loadPlugin(pathfinder.pathfinder)
# print("Started mineflayer")
#
#
# @On(bot, 'spawn')
# def handle(*args):
#     print("I spawned 👋")
#     movements = pathfinder.Movements(bot)
#
#
# @On(bot, 'chat')
# def handle(*args):
#     print("Position of the bot: ", bot.entity.position)
#     print("X : ", bot.entity.position.x)
#
#     @On(bot, 'chat')
#     def handleMsg(this, sender, message, *args):
#         print("Got message", sender, message)
#         if sender and (sender != BOT_USERNAME):
#             bot.chat('Hi, you said ' + message)
#             if 'come' in message:
#                 player = bot.players[sender]
#                 print("Target", player)
#                 target = player.entity
#                 if not target:
#                     bot.chat("I don't see you !")
#                     return
#                 pos = target.position
#                 bot.pathfinder.setMovements(movements)
#                 bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, RANGE_GOAL))
#
#
# @On(bot, "end")
# def handle(*args):
#     print("Bot ended!", args)

# createBot("Clone")

############################################################################
# from sys import exit
#
# from mcpi.minecraft import Minecraft
#
# from bot import Bot
#
# mc = Minecraft.create(address="localhost", port=4711)
# bot = []
#
# players_ids = mc.getPlayerEntityIds()
# print(len(players_ids), " entities available.")
# number = len(players_ids)
# mc.postToChat("%s entities available." % number)
# # mc.postToChat("stop")
# for id_p in players_ids:
#     mc.postToChat("Entity player nb : %s" % id_p)
#


# while True:
# players_ids = mc.getPlayerEntityIds()
# if len(players_ids) > number:
#     bot.append(Bot())
#     bot[len(bot)-1].connect_bot()
#     number = len(players_ids)
#     mc.postToChat("Bot connected")
# elif len(players_ids) < number:
#     bot[len(bot)-1].disconnect_bot()
#     bot.pop()
#     number = len(players_ids)
#     mc.postToChat("Bot disconnected")
# else:
#     pass
#
# botAI = Bot()
# botAI.bot.connect_bot()
#
# botAI.bot.on('chat', botAI.bot.chat(f"Someone joined! It's {botAI.bot.username}"))
#


# for post in mc.events.pollChatPosts():
#
#     if post.message == "connect":
#         print("Connection...")
#         botAI = InitialiseBot()
#
#     if post.message == "stop" and botAI != []:
#         print("Stopping...")
#         botAI.disconnect()
#
#     if post.message == "kill":
#         print("Killing...")
#         botAI.bot.chat("I'm dying")
#
#     elif botAI == []:
#         print("No bot connected")
#     else:
#         pass
#         # botAI.chat('pas compris')

# The project is divided in 3 parts :
# 1. How to get the data from the game
# 2. How to implement the AI with basic rules set
# 3. How to implement the AI with Q-Learning tables

# 1. How to get the data from the game
# The first step is to get the data from the game
# This is the most difficult part of the project
# The data can be get from the game in 2 ways :
# 1.1. By using a library like OpenAI Gym
# 1.2. By using the Minecraft API

# 1.1. By using a library like OpenAI Gym
# The first way to get data from the game is by using a library like OpenAI Gym
# The problem is that OpenAI Gym is not made for Minecraft
# Moreover, I don't know if it is possible to use OpenAI Gym for Minecraft
# The first step is to find a way to use OpenAI Gym for Minecraft
# If it is not possible to use OpenAI Gym for Minecraft, I will use the Minecraft API

# 1.2. By using the Minecraft API
# The second way to get data from the game is by using the Minecraft API
# The Minecraft API is made for Minecraft and is very easy to use
# The problem is that the Minecraft API is not made for AI
# The first step is to find a way to use the Minecraft API for AI
# If it is not possible to use the Minecraft API for AI, I will use OpenAI Gym

# 2. How to implement the AI with basic rules set The second step is to implement the AI with basic rules set The
# basic rules set will be very easy to implement The basic rules set will be made for the first version of the AI The
# first version of the AI will be very simple The first version of the AI will be able to play Minecraft but it will
# not be good The first version of the AI will be able to play Minecraft but it will not be able to get a good score
# The first version of the AI will be able to play Minecraft but it will not be able to learn The first version of
# the AI will be able to play Minecraft but it will not be able to learn how to play Minecraft The first version of
# the AI will be able to play Minecraft but it will not be able to learn how to get a good score The first version of
# the AI will be able to play Minecraft but it will not be able to learn how to play Minecraft and get a good score

# 3. How to implement the AI with Q-Learning tables
# The third step is to implement the AI with Q-Learning tables
# The Q-Learning tables will be very difficult to implement
# The Q-Learning tables will be made for the second version of the AI
