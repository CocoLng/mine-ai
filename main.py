####################################################
# cd .\server\
# java -jar .\spigot-1.19.3.jar
####################################################

import os
from time import sleep

from dotenv import load_dotenv
from mcpi.minecraft import Minecraft

load_dotenv()

mc = Minecraft.create(address=os.getenv('IP'), port=4711)

# Constantly grab the player's position and create
# a new stone block underneath him/her
while True:
    x, y, z = mc.player.getPos()
    
    # Debug
    print("x: {}, y: {}, z: {}".format(x, y, z))
    
    mc.setBlock(x, y - 1, z, 1)
    sleep(0.1)

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
