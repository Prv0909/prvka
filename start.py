import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('BEATBOX'))
	print('bot is ready')
	
@client.command()
async def timer(ctx, seconds):
    try:
        secondint = int(seconds)
        if secondint > 300:
            await ctx.send("I don't think I can go over 5 mins.")
            raise BaseException
        if secondint <= 0:
            await ctx.send("I don't think I can do negatives")
            raise BaseException

        message = await ctx.send(f"Timer: {seconds}")

        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content="Ended!")
                break

            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
        await ctx.send(f"{ctx.author.mention}, Your countdown has been ended!")
    except ValueError:
        await ctx.send('You must enter a number!')	    	
	    	    			
client.run('NzU4OTU4OTA5MTg4MDc5NjM5.X22hkA.rBz5yWSqYR55z2-ijkQ60digelk')