import discord
import asyncio
import os
from discord.ext import commands

client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-------------------")
    await client.change_presence(game=discord.Game(name= '애플봇 작동주우우우웅', type=1))


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!안녕'):
        msg = '안녕! {0.author.mention} 아! 반가워!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!명령어'):
        await client.send_message(message.channel, "```애플봇 명령어 모으으으음!```")
        await client.send_message(message.channel, "!제작자 : 애플봇 제작자를 보여줍니다. ")
        await client.send_message(message.channel, "!홍보 : 홍보에 대한 정보를 알려줍니다. ")
        await client.send_message(message.channel, "더 많은 명령어를 만들지 못해 죄송합니다.")
        await client.send_message(message.channel, "더 많이 일하여 많은 명령어를 만들겠습니다. 감사합니다.")

    if message.content.startswith('!애플'):
        await client.send_message(message.channel, "루슬라임블 : 애쁘린데요 ")
        await client.send_message(message.channel, "피프티 : ??? ")
        await client.send_message(message.channel, "멜롱풉딩 : 네? ")
        await client.send_message(message.channel, "ApplegamerPRO : ApplegamerPRO 입니닷 ")

    if message.content.startswith('!홍보'):
        await client.send_message(message.channel, "홍보하실거면 홍보방에 해주시고 ")
        await client.send_message(message.channel, "이 디스코드방을 다른 디스코드 방이나 ")
        await client.send_message(message.channel, "유튜브를 통해 이 방을 홍보할시 ")
        await client.send_message(message.channel, "관리자들의 사랑과 홍보자 랭크를 드립니다. ")
        await client.send_message(message.channel, "사랑이 받기 싫다고요? 그러면 그냥 ")
        await client.send_message(message.channel, "홍보자 랭크 드릴게요 ㅋㅋㅋㅋㅋ ")

    if message.content.startswith('!제작자'):
        await client.send_message(message.channel, "```제작자 목록입니다.```")
        await client.send_message(message.channel, "개발자 : ApplegamerPRO ")
        await client.send_message(message.channel, "일러스트 : 담크리의 다우 ")
        await client.send_message(message.channel, "감독 : 루슬라임블 ")
        await client.send_message(message.channel, "제작자는 언제든지 참여가 가능합니다." )

    if message.content.startswith('!삐흐봇'):
        await client.send_message(message.channel, "삐흐봇은 제작자 ApplegamerPRO 가 안만들어줘서 삐흐님이 파일을 지웠습니다.-삐흐봇... 명복을 빕니다...-")

    if message.content.startswith('!골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)

    if message.content.startswith('!관리자호출'):
        await client.send_message(message.channel, '관리자를 호출합니드아아아아!(귀찮..,)     <@309605383197032448> <@453788126712823808> <@368383510853189635>')

    if message.content.startswith('!호출애플'):
        await client.send_message(message.channel, '애플님을 호출할게여우ㅡ우  <@309605383197032448>')

    if message.content.startswith('!친구들아!'):
        await client.send_message(message.channel, '이제부터 한 말은 실친이 친겁니다 : 애쁘리바보')

access_token = os.environ["BOT TOKEN"]
client.run(access_token)
