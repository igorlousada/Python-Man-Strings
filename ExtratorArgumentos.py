class ExtratorArgumentosUrl:
    def __init__(self,url):
        if(self.url_valida(url)):
            self.url = url.lower()
        else:
            raise LookupError("Url Invalida")    

    @staticmethod
    def url_valida(url):

        if (url):
            return True
        else:
            return False

    def __str__(self):
        return "objeto criado"

    def extrai_argumentos(self):
        moeda_origem = 'moedaorigem='
        moeda_destino = 'moedadestino='
        indiceInicialMoedaOrigem = self.busca_moeda(moeda_origem)
        indiceFinalMoedaOrigem =  self.url.find('&')
        indiceFinalMoedaDestino = self.url.find('&',indiceFinalMoedaOrigem + 1)
        indiceInicialMoedaDestino = self.busca_moeda(moeda_destino)
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]
        if(moedaOrigem == "moedadestino"):
            self.troca_moeda_origem()
            indiceInicialMoedaOrigem = self.busca_moeda(moeda_origem)
            indiceFinalMoedaOrigem =  self.url.find('&')
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]    
        valor = self.extrai_valor()
        return moedaOrigem,moedaDestino,valor

    def busca_moeda(self,moeda_buscada):
        return  self.url.find(moeda_buscada) + len(moeda_buscada)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino","real",1)  
        print(self.url)
        return None
    def extrai_valor(self):
        busca_valor = 'valor='
        indice_inicial_valor = self.busca_moeda(busca_valor)
        valor = self.url[indice_inicial_valor:]
        return valor
        #print(valor)



