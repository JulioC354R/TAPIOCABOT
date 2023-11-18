#importando Discord
import discord

#importando async
import asyncio

#importando Intents
from discord.flags import Intents
from tokenDisc import Token


#importando os comandos do discord
from discord.ext import commands

class Bot:
    
    def iniciar_bot():
        #intents são as permissões do bot, aqui vou adicionar as todas as permissões
        intents = discord.Intents.all()

        #estou dizendo que a váriavel Tapioca vai receber a função commands.Bot, aqui temos os
        #prefixo do comando (como os comandos vão ser chamados no discord)
        TAPIOCA = commands.Bot(command_prefix= '!', intents= intents)


        # função assincrona, quando chamarem ola num determinado canal, o bot vai executar esse trecho

        @TAPIOCA.command(name= 'ola')


        async def ola(context):
            #aqui diz, no canal que a mensagem chegou, mande:

            #sempre usar o await quando for mandar uma mensagem
            await context.message.channel.send('Pegou carambolas')


        #pedindo para executar o bot, utilizando o token
        TAPIOCA.run(Token.token)

