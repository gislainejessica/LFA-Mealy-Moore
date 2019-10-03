
class Mealy(object):
    ''' Receber paramentros para inicializar a classes com os valores lidos
        Por enquanto, a classe tá inicializando com valores default
    '''
    def __init__(self, nome ="", estados = [], alfabetoEntrada= [], inicial= [], finais= [], alfabetoSaida= [], transicao=[]):
        self.nome = nome
        self.estados = estados
        self.alfabetoEntrada = alfabetoEntrada
        self.inicial = inicial
        self.finais = finais
        self.alfabetoSaida = alfabetoSaida
        self.transicao = transicao

        # self.nome = 'Mealy'
        # self.estados = ['s*', 's1', 's2']
        # self.alfabetoEntrada = ['a','b','c']
        # self.inicial = ['s*']
        # self.finais = ['--']
        # self.alfabetoSaida = ['T', 'F', 'O']
        ''' Função de Transição... Thinking '''


    '''Getters e Setters'''

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

    def get_transicao(self):
            return self.transicao

    def set_transicao(self, transicao):
        self.transicao = transicao


    ''' Converte essa classe para Moore'''
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

        for trans in self.transicao:
            arquivo.write((" ".join(trans)) + '\n')

        arquivo.close()

        return arquivo
