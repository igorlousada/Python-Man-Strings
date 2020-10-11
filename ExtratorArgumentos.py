class ExtratorArgumentosUrl:
    def __init__(self,url):
        if(self.url_valida(url)):
            self.url = url
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

    def ExtraiArgumentos(self):

        indiceFinalMoedaDestino = 
        indiceInicialMoedaDestino = 

        indiceInicialMoedaOrigem = 
        indiceFinalMoedaOrigem =  