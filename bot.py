import discord

class DiscordBot(discord.Client):
	async def on_ready(self):
		print(f'Logged on as {self.user}!')

	async def on_message(self, message):
		print(f'Message from {message.author}: {message.content}')

client = DiscordBot()
client.run('NzE1NjYyNzg1MjExNjYyNDQ2.XtAe6A.iGUxNbCNA08dTCONDOg6qr9v0u0')