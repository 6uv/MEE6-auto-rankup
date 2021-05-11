import time, discord

client = discord.Client()

counter = 1

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} | {client.user.id}')
    print('----------------')
    while True:
        global counter
        msgchannel = client.get_channel(YOUR CHANNEL ID HERE) # channel ID goes here, dont put it in " " or ' '
        await msgchannel.send('YOUR MESSAGE HERE') # you can edit the message here, keep it in " "
        print(f'[{counter}] Sent message!')
        counter+=1
        time.sleep(30) # alter the speed to your liking, the lower the speed, the higher chance of being banned

try:
    client.run("YOUR TOKEN HERE", bot=False) # token goes inbetween " "
except Exception as e:
    print(f'Error\n\nTraceback\n{str(e)}')