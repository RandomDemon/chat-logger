import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA2MTExNDM0NDgyNzUxODk4Ng.G8xQx5._0xreX9aoQ6pj37FGj95JDWK1wjwR_XC1Hu9t0')
