import discord
import asyncio
import urllib3
import json

from discord import Game

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = discord.Client()
http = urllib3.PoolManager(10,
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'})
# The following is an example. Add as many sevrvers as you would like to the array.
servers = [["STRP #1", "66.70.180.161:30120", False],
           ["STRP #2", "66.70.180.161:30121", False],
           ["STRP #3", "66.70.180.161:30122",False],
           ["STRP Whitelist #1", "66.70.180.161:30123", False]]


def server_online(ip):
    req = http.request('GET', 'https://servers-live.fivem.net/api/servers/single/' + ip)
    code = req.status
    if code == 200:
        return True
    return False


def server_json(ip):
    if server_online(ip):
        req = http.request('GET', 'https://servers-live.fivem.net/api/servers/single/' + ip)
        return json.loads(req.data.decode('utf-8'))


async def server_status_check():
    await client.wait_until_ready()
    channel = discord.Object(id='ANNOUNCEMENT_CHANNEL_ID_HERE')
    while not client.is_closed:
        for server_id, server in enumerate(servers):
            if not server_online(server[1]) and server[2] is False:
                print(server[0] + " " + server[1] + " OFFLINE")
                await client.send_message(channel, ":x: " + server[0] + "is now Offline! Standby for outage "
                                                                        "information! :x:")
                servers[server_id][2] = True
            if server[2] is True and server_online(server[1]):
                print(server[0] + " " + server[1] + " ONLINE")
                await client.send_message(channel, ":white_check_mark: " + server[0] + "is now Online! "
                                                                                       ":white_check_mark:")
                servers[server_id][2] = False
    await asyncio.sleep(10)


async def server_count_status():
    await client.wait_until_ready()
    while not client.is_closed:
        player_count = 0
        for server_id, server in enumerate(servers):
            player_count += server_json(server[1])["Data"]["clients"]
        await client.change_presence(game=Game(name=str(player_count) + " players on STRP"))
    await asyncio.sleep(5)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(server_count_status())
client.loop.create_task(server_status_check())
client.run('TOKEN')
