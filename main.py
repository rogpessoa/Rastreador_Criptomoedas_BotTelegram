from datetime import datetime
import locale
from time import sleep
from classes import CoinGeckoAPI, TelegramBot
locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')


id_moeda = input('Qual moeda deseja rastrear? ')
valor_minimo = int(input('Qual o valor minimo que deseja rastrear? '))
valor_maximo = int(input('Qual valor maximo que deseja rastrear? '))

api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3/')
bot_telegram = TelegramBot(token='digite o token', chat_id=digite o chatid)

#API ficara rodando sempre, mas sera definido atraves do sleep um tempo para ser verificado novamente
while True:
    if api.ping():
        print('API online...')
        #O retorno da API eh preco e atualizado em na mesma ordem que esta abaixo, dessa forma atribui cada valor
        preco, atualizado_em = api.consulta_preco(id_moeda=id_moeda)
        print('Consulta realizada com sucesso...')
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = None

        if preco < valor_minimo:
            mensagem = f'*Cotação do {id_moeda}*:\n\t*Preço*: R${preco}\n\t *Horário*: {data_hora}' \
                       f'\n\t*Motivo*: Valor menor que o minimo'

        elif preco > valor_maximo:
            mensagem = f'*Cotação do {id_moeda}*:\n\t*Preço*: R${preco}\n\t *Horário*: {data_hora}' \
                       f'\n\t*Motivo*: Valor maior que o maximo'

        if mensagem:
            bot_telegram.envia_mensagem(texto_markdown=mensagem)

    else:
        print('API offline, tente novamente mais tarde!')

    sleep(300)
    
