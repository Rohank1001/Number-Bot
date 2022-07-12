import discord
import os
from tabulate import tabulate

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    tries=0
    top = ["Name", "Tries"]
    if '!guess' in message.content:
      await message.channel.send("Check your Dm's")
      
      import random
      Guess=0
      numb=random.randint(1,100)
      await message.author.send(numb)
      
      while  Guess!=numb: 
        await message.author.send('Guess a number between 1 and 100')
        x=await client.wait_for('message')
        Guess=int(x.content)
    
        if (Guess<numb):
          await message.author.send('Your guess was too low, try again')
          tries=tries+1 
          
        elif (Guess>numb):
          await message.author.send('Your guess was too high, try again')
          tries=tries+1

          
      tries=tries+1
      await message.author.send('Congratulations you got the number in '+str(tries)+' tries, enter your name for entry into our leaderboard')
      if message.author == client.user:
        return
      else:
        z=await client.wait_for('message')
          
        
        
        mydata = [[z.content,tries]]
        table=((tabulate(mydata, headers=top, tablefmt="simple")))
        await message.author.send(table+"\nType !leaderboard in your discord server to see the full table")
        
        f = open("ranking.txt", "a")
        f.write("\n")
        f.write("\n"+table)
        f.close()
    
  
    if "!leaderboard" in message.content:
      f = open("ranking.txt", "r")
      await message.channel.send(f.read())

client.run(os.environ['TOKEN'])
