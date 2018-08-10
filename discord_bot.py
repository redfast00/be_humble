import discord
import asyncio
from humblebundle import get_free_game_names
from config import GAME_THREAD_CHANNEL_ID, TOKEN

TIMEOUT = 60 * 60

client = discord.Client()


async def humble_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id=GAME_THREAD_CHANNEL_ID)
    already_seen = set()
    while not client.is_closed:
        print("checking new games")
        free_games = set(get_free_game_names())
        # Check if there are free games right now and if we haven't seen them
        if free_games and not free_games.issubset(already_seen):
            print("Sending message...")
            message = '<@&461088717101334539> FREE right now: {} https://humblebundle.com/store/search?sort=discount'.format(' + '.join(free_games))
            await client.send_message(channel, message)
            already_seen.update(free_games)
        await asyncio.sleep(TIMEOUT)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(humble_background_task())
client.run(TOKEN)
