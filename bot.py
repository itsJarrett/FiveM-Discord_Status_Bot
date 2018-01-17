import discord
import asyncio
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = discord.Client()
http = urllib3.PoolManager(10, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'})

offline1 = False
offline2 = False
offline3 = False
offline4 = False
message1 = False
message2 = False
message3 = False
message4 = False

async def server_status_check():
    await client.wait_until_ready()
    channel = discord.Object(id='ANNOUNCEMENT_CHANNEL_ID_HERE')
    global offline1
    global offline2
    global offline3
    global offline4
    global message1
    global message2
    global message3
    global message4
    while not client.is_closed:
        req1 = http.request('GET','https://servers-live.fivem.net/api/servers/single/66.70.180.161:30121')
        code1 = req1.status
        if code1 != 200 and message1 == False:
            if offline1 == False:
                await client.send_message(channel, "STRP #1 is Offline. Standby for outage information. :x:")
                offline1 = True
                message1 = True
        else:
            if offline1 == True and code1 == 200:
                await client.send_message(channel, "STRP #1 is now back Online. :white_check_mark:")
                offline1 = False
                message1 = False

        req2 = http.request('GET','https://servers-live.fivem.net/api/servers/single/66.70.180.161:30121')
        code2 = req2.status
        if code2 != 200 and message2 == False:
            if offline2 == False:
                await client.send_message(channel, "STRP #2 is Offline. Standby for outage information. :x:")
                offline2 = True
                message2 = True
        else:
            if offline2 == True and code2 == 200:
                await client.send_message(channel, "STRP #2 is now back Online. :white_check_mark:")
                offline2 = False
                message2 = False

        req3 = http.request('GET','https://servers-live.fivem.net/api/servers/single/66.70.180.161:30123')
        code3 = req3.status
        if code3 != 200 and message3 == False:
            if offline3 == False:
                await client.send_message(channel, "STRP Whitelist #1 is Offline. Standby for outage information. :x:")
                offline3 = True
                message3 = True
        else:
            if offline3 == True and code3 == 200:
                await client.send_message(channel, "STRP Whitelist #1 is now back Online. :white_check_mark:")
                offline3 = False
                message3 = False

        req4 = http.request('GET','https://servers-live.fivem.net/api/servers/single/66.70.180.161:30122')
        code4 = req4.status
        if code4 != 200 and message4 == False:
            if offline4 == False:
                await client.send_message(channel, "STRP Whitelist #2 is Offline. Standby for outage information. :x:")
                offline4 = True
                message4 = True
        else:
            if offline4 == True and code4 == 200:
                await client.send_message(channel, "STRP Whitelist #2 is now back Online. :white_check_mark:")
                offline4 = False
                message4 = False
    await asyncio.sleep(5)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(server_status_check())
client.run('TOKEN_HERE')
