#import os
import discord
from slackclient import SlackClient

#Tokens, insert your own

DTOKEN = 'foo'
STOKEN = 'bar' #os.environ['bar']

#Channels

DCHANNEL = 'allchat'
SCHANNEL = 'allchat'

#Bots

sbot = SlackClient(STOKEN)
dbot = discord.Client()

##############################
#           SHARED           #
##############################



##############################
#           SLACK            #
##############################

#sends slack message to discord
def slack_to_discord():
    return


##############################
#           DISCORD          #
##############################

#sends discord message to slack
def discord_to_slack(discordmessage):
    
    return


@dbot.event
async def on_message(message):
    if message.author == dbot.user:
        return

    else:
        discord_to_slack(message)
        return


##############################
#           RUN              #
##############################
dbot.run(DTOKEN)


