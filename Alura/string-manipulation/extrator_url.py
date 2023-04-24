import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)

    def __len__(self):
        return len(self.url)

    def __str__(self):
        valor_dolar = 5.5
        moeda_origem = self.get_valor_parametro("moedaOrigem")
        moeda_destino = self.get_valor_parametro("moedaDestino")
        quantidade = self.get_valor_parametro("quantidade")

        if moeda_destino == "dolar" and moeda_origem == "real":
            return "moeda Origem: " + moeda_origem + "\n" + \
                "moeda Destino: " + moeda_destino + "\n" + \
                "quantidade: " + str(float(quantidade)/valor_dolar)
        elif moeda_destino == "real" and moeda_origem == "dolar":
            return "moeda Origem: " + moeda_origem + "\n" + \
                   "moeda Destino: " + moeda_destino + "\n" + \
                   "quantidade: " + str(float(quantidade) * valor_dolar)
        else:
            return "conversão não disponível"

    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL é inadequada")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor