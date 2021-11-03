# Instalar o Kivy COMANDO:"pip install kivy"
# Depois instalar o requests COMANDO:"pip install requests" porque não vem instalado

# importar o App, Builder (Gui)
# Criar o nosso  aplicativo
# Criar a função build

from os import link
from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.Kv")


class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"

    def pegar_cotacao(self, moeda):
        link = f"http://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run()
