import asyncio
import discord
import logging
import random
import string

logging.basicConfig(level=logging.INFO)

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    smiteNameList = ["smite", "smizzle"]
    if any(word in message.content.lower() for word in smiteNameList):
        currentPlayers = getCurrentPlayers(discord.Game(name='SMITE'), message.server.members)
        if(len(currentPlayers) != 0):
            currentPlayers.insert(0, 'The following users are playing SMITE')
            msg = '\n'.join(currentPlayers)
            await client.send_message(message.channel, msg)

    pubgNameList = ["pubg", "battlegrounds"]
    if any(word in message.content.lower() for word in pubgNameList):
        currentPlayers = getCurrentPlayers(discord.Game(name='PUBG'), message.server.members)
        if(len(currentPlayers) != 0):
            currentPlayers.insert(0, 'The following users are playing PUBG')
            msg = '\n'.join(currentPlayers)
            await client.send_message(message.channel, msg)

    # if message.content.startswith('!hello'):
    #     msg = 'Hello {0.author.mention}'.format(message)
    #     await client.send_message(message.channel, msg)
    if message.author.id == '364136398695170049':
        await client.change_nickname(message.author, randomizeNickname(message.author.name))


@client.event
async def on_ready():
    logging.info('Logged in as')
    logging.info(client.user.name)
    logging.info(client.user.id)
    logging.info('Invite: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'.format(client.user.id))
    logging.info('------')


def main():
    client.run('MzY0MDkwNDc4MTU4OTM4MTE2.DLKvNQ.99xu8JCpS8wO9UjSipesDKAecX4')


def getCurrentPlayers(game, membersList):
    currentPlayers = []
    for member in membersList:
        if game == member.game:
            currentPlayers.append(member.display_name)
    return currentPlayers


def randomizeNickname(nickname):
    nickname = randomLetterSwapCase(nickname)
    nickname = randomLetterInsert(nickname)
    return(nickname)


def randomLetterSwapCase(word):
    randomSlice = random.randint(0, len(word) - 1)
    halfA = word[:randomSlice]
    midpoint = word[randomSlice].swapcase()
    halfB = word[randomSlice + 1:]
    return(halfA + midpoint + halfB)


def randomLetterInsert(word):
    randomLetter = random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=1)[0]

    randomSlice = random.randint(0, len(word) - 1)
    halfA = word[:randomSlice]
    halfB = word[randomSlice:]
    return(halfA + randomLetter + halfB)


if __name__ == "__main__":
    main()
