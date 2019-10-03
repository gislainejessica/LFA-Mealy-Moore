from typing import TextIO


class Moore(object):
    """ Receber paramentros para inicializar a classes com os valores lidos
        Por enquanto, a classe tá inicializando com valores default
    """

    def __init__(self, nome="", estados=[], alfabetoEntrada=[], inicial=[], finais=[], alfabetoSaida=[],
                 transicaoEntrada=[], transicaoSaida=[]):
        self.nome = nome
        self.estados = estados
        self.alfabetoEntrada = alfabetoEntrada
        self.inicial = inicial
        self.finais = finais
        self.alfabetoSaida = alfabetoSaida
        self.transicaoEntrada = transicaoEntrada
        self.transicaoSaida = transicaoSaida

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_estados(self):
        return self.estados

    def set_estados(self, estados):
        self.estados = estados

    def get_alfabetoEntrada(self):
        return self.alfabetoEntrada

    def set_alfabetoEntrada(self, alfabetoEntrada):
        self.alfabetoEntrada = alfabetoEntrada

    def get_inicial(self):
        return self.inicial

    def set_inicial(self, inicial):
        self.inicial = inicial

    def get_finais(self):
        return self.finais

    def set_finais(self, finais):
        self.finais = finais

    def get_alfabetoSaida(self):
        return self.alfabetoSaida

    def set_alfabetoSaida(self, alfabetoSaida):
        self.alfabetoSaida = alfabetoSaida

    def get_transicaoEntrada(self):
        return self.transicaoEntrada

    def set_transicaoEntrada(self, transicaoEntrada):
        self.transicaoEntrada = transicaoEntrada

    def get_transicaoSaida(self):
        return self.transicaoSaida

    def set_transicaoSaida(self, transicaoSaida):
        self.transicaoSaida = transicaoSaida

    def le_moore(self, nomeEntrada):
        arqEntrada = open(nomeEntrada, 'r')
        self.set_nome(arqEntrada.readline().rstrip('\n'))

        ''' Logica para inicializar classe com valores'''
        estados = arqEntrada.readline().rstrip('\n').split(' ')
        self.set_estados(estados)

        alfabetoEntrada = arqEntrada.readline().rstrip('\n').split(' ')
        self.set_alfabetoEntrada(alfabetoEntrada)

        inicial = arqEntrada.readline().rstrip('\n').split(' ')
        self.set_inicial(inicial)

        finais = arqEntrada.readline().rstrip('\n').split(' ')
        self.set_finais(finais)

        alfabetoSaida = arqEntrada.readline().rstrip('\n').split(' ')
        self.set_alfabetoSaida(alfabetoSaida)

        transicaoEntrada = []
        for linha in arqEntrada.readlines():
            linha = linha.rstrip('\n')
            transicaoEntrada.append(linha.split(' '))
            if linha == '-----':
                transicaoEntrada.remove(linha.split(' '))
                self.set_transicaoEntrada(transicaoEntrada)

        transicaoSaida = []
        for linha in arqEntrada.readlines():
            linha = linha.rstrip('\n').split(' ')
            transicaoSaida.append(linha)

        self.set_transicaoSaida(transicaoSaida)
        

        ''' Fechando o arquivo'''
        arqEntrada.close()
        return 0

    ''' Converte essa classe para Mealy'''

    def converte(self):
        return

    ''' Imprime seus atributos em um arquivo, formatado no padrão pedido'''

    def imprime(self, nome_arquivo):
        arquivo = open(nome_arquivo, "a")

        arquivo.write(self.get_nome() + '\n')
        arquivo.write((" ".join(self.get_estados())) + '\n')
        arquivo.write((" ".join(self.get_alfabetoEntrada())) + '\n')
        arquivo.write((" ".join(self.get_inicial())) + '\n')
        arquivo.write((" ".join(self.get_finais())) + '\n')
        arquivo.write((" ".join(self.get_alfabetoSaida())) + '\n')

        for transE in self.get_transicaoEntrada():
            arquivo.write((" ".join(transE)) + '\n')
        
        arquivo.write('-----\n')

        for transS in self.get_transicaoSaida():
            arquivo.write((" ".join(transS)) + '\n')

        ''' Fechando o arquivo'''
        arquivo.close()

        return 0
