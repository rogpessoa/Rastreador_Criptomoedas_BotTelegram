import requests
import telegram


#Classe CoinGecko vai consultar a API, realizar ping e consultar as moedas que o usuario desejar.
class CoinGeckoAPI:
    def __init__(self, url_base: str):
        """
        Funcao para iniciar a API, usuario deve passar a URL para iniciar a pesquisa
        :param url_base: URL deve ser passada no formato str para iniciar a pesquisa na API
        """
        self.url_base = url_base

    def ping(self) -> bool:
        """
        Funcao que vai retornar um valor True ou False, vai consultar se o status da consulta a API foi 200
        :return: Retorna valor Booleano, se for status 200 operacao foi bem sucesso.
        """
        print('Verificando se API esta online...')
        url = f'{self.url_base}/ping'
        return requests.get(url).status_code == 200

    def consulta_preco(self, id_moeda: str) -> tuple:
        """
        Funcao que vai receber o id da moeda e atraves disso pesquisar na URL ja tratada.
        :param id_moeda: Usuario passa o id da moeda que deseja consultar e a funcao consulta na API da CoinGecko
        :return: Vai retornar o preco em R$ da moeda pesquisada e a data em que foi pesquisado
        """
        print(f'Consultado preço da moeda ID: {id_moeda}')
        url = f'{self.url_base}/simple/price?ids={id_moeda}&vs_currencies=BRL&include_last_updated_at=true'
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados_moeda = resposta.json().get(id_moeda, None)
            preco = dados_moeda.get('brl', None)
            atualizado_em = dados_moeda.get('last_updated_at', None)
            return preco, atualizado_em

        else:
            raise ValueError('Codigo de resposta diferente do esperado.')


class TelegramBot:
    def __init__(self, token: str, chat_id: int):
        """
        Metodo para criar o Bot atraves do FatherBot do telegram.
        :param token: Enviado no momento que se cria o Bot e deve ser mantido em sigilo
        :param chat_id: Retirado atraves de consulta da API
        """
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id

    def envia_mensagem(self, texto_markdown: str):
        """
        Metodo para enviar mensagem ao ususario telegram que interagir com o bot
        :param texto_markdown: Mensagem que sera enviada
        :return:
        """
        self.bot.send_message(
            text=texto_markdown,
            chat_id=self.chat_id,
            parse_mode=telegram.ParseMode.MARKDOWN)



