from extrator_url import ExtratorURL

url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"

objeto_url = ExtratorURL(url)
objeto_url_2 = ExtratorURL(url)

quantidade = objeto_url.get_valor_parametro("quantidade")
print(type(float(quantidade)))
valor = objeto_url.get_valor_parametro("moedaDestino")

print(id(objeto_url))
print(id(objeto_url_2))
print(objeto_url)