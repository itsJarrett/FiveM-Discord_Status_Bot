import discord
import asyncio
import urllib3
urllib3.disable_warnings()


client = discord.Client()
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
http = urllib3.PoolManager(10, headers=user_agent)

offline1 = False
message1 = False
offline2 = False
message2 = False
offline3 = False
message3 = False
offline4 = False
message4 = False

async def server_status_check():
    await client.wait_until_ready()
    channel = discord.Object(id='ANNOUNCEMENT_CHANNEL_ID_HERE')
    global offline1
    global message1
    global offline2
    global message2
    global offline3
    global message3
    global offline4
    global message4
    while not client.is_closed:
        req1 = http.request('GET','https://servers-live.fivem.net/api/servers/single/66.70.180.161:30120')
        code1 = req1.status
        if code1 != 200:
            if offline1:
                client.send_message("STRP #1 is Offline. Standby for outage information. :x:")
                message1 = True
            offline1 = True
        else:
            if message1:
                client.send_message("STRP #1 is now back Online. :white_check_mark:")
                message1 = False
            offline1 = False

        req2 = http.request('GET','https://servers-live.fivem.net/api/servers/single/66.70.180.161:30121')
        code2 = req2.status
        if code2 != 200:
            if offline2:
                client.send_message("STRP #2 is Offline. Standby for outage information. :x:")
                message2 = True
            offline2 = True
        else:
            if message2:
                client.send_message("STRP #2 is now back Online. :white_check_mark:")
                message2 = False
            offline2 = False

        req3 = http.request('GET','https://servers-live.fivem.net/api/servers/single/66.70.180.161:30123')
        code3 = req3.status
        if code3 != 200:
            if offline3:
                client.send_message("STRP Whitelist #1 is Offline. Standby for outage information. :x:")
                message3 = True
            offline3 = True
        else:
            if message3:
                client.send_message("STRP Whitelist #1 is now back Online. :white_check_mark:")
                message3 = False
            offline3 = False

        req4 = http.request('GET','https://servers-live.fivem.net/api/servers/single/66.70.180.161:30122')
        code4 = req4.status
        if code4 != 200:
            if offline4:
                client.send_message("STRP Whitelist #2 is Offline. Standby for outage information. :x:")
                message4 = True
            offline4 = True
        else:
            if message4:
                client.send_message("STRP Whitelist #2 is now back Online. :white_check_mark:")
                message4 = False
            offline4 = False
    await asyncio.sleep(5)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(server_status_check())
client.run('token')
