import discord
import asyncio
import urllib2


client = discord.Client()
offline1 = false
messsage1 = false
offline2 = false
messsage2 = false
offline3 = false
messsage3 = false
offline4 = false
messsage4 = false

async def server_status_check():
    await client.wait_until_ready()
    channel = discord.Object(id='ANNOUNCEMENT_CHANNEL_ID_HERE')
    while not client.is_closed:
        req1 = urllib2.Request('https://servers-live.fivem.net/api/servers/single/66.70.180.161:30120')
        req1.add_header('User-agent', 'Mozilla 5.10')
        response1 = urllib2.urlopen(req1)
        json1 = response1.read()
        code1 = response1.getcode()
        if code1 != 200:
            if offline1:
                client.send_message("STRP 1 #1 is Offline. Standby for outage information. :x:")
                message1 = true
            offline1 = true
        else
            if message1:
                client.send_message("STRP #1 is now back Online. :white_check_mark:")
                message1 = false
            offline1 = false

        req2 = urllib2.Request('https://servers-live.fivem.net/api/servers/single/66.70.180.161:30121')
        req2.add_header('User-agent', 'Mozilla 5.10')
        response2 = urllib2.urlopen(req2)
        json2 = response2.read()
        code2 = response2.getcode()
        if code2 != 200:
            if offline2:
                client.send_message("STRP #2 is Offline. Standby for outage information. :x:")
                message2 = true
            offline2 = true
        else
            if message2:
                client.send_message("STRP #2 is now back Online. :white_check_mark:")
                message2 = false
            offline2 = false

        req3 = urllib2.Request('https://servers-live.fivem.net/api/servers/single/66.70.180.161:30123')
        req3.add_header('User-agent', 'Mozilla 5.10')
        response3 = urllib2.urlopen(req3)
        json3 = response3.read()
        code3 = response3.getcode()
        if code3 != 200:
            if offline3:
                client.send_message("STRP Whitelist #1 is Offline. Standby for outage information. :x:")
                message3 = true
            offline3 = true
        else
            if message3:
                client.send_message("STRP Whitelist #1 is now back Online. :white_check_mark:")
                message3 = false
            offline3 = false

        req4 = urllib2.Request('https://servers-live.fivem.net/api/servers/single/66.70.180.161:30122')
        req4.add_header('User-agent', 'Mozilla 5.10')
        response4 = urllib2.urlopen(req4)
        json4 = response4.read()
        code4 = response4.getcode()
        if code4 != 200:
            if offline4:
                client.send_message("STRP Whitelist #2 is Offline. Standby for outage information. :x:")
                message4 = true
            offline4 = true
        else
            if message4:
                client.send_message("STRP Whitelist #2 is now back Online. :white_check_mark:")
                message4 = false
            offline4 = false
        await asyncio.sleep(15)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(server_status_check()))
client.run('token')
