from ExtratorArgumentos import ExtratorArgumentosUrl
url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=700"
#url = None
#print(ExtratorArgumentosUrl.url_valida(url))
#print(argumento)  
valor_moeda = ExtratorArgumentosUrl(url)
var = valor_moeda.extrai_argumentos()
print(var[1])
print(len(valor_moeda))
