
class Mealy(object):
    """ Receber paramentros para inicializar a classes com os valores lidos
        Por enquanto, a classe tá inicializando com valores default
    """

    def __init__(self, nome="", estados=[], alfabetoEntrada=[], inicial=[], finais=[], alfabetoSaida=[], transicao=[]):
        self.nome = nome
        self.estados = estados
        self.alfabetoEntrada = alfabetoEntrada
        self.inicial = inicial
        self.finais = finais
        self.alfabetoSaida = alfabetoSaida
        self.transicao = transicao

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

    def le_mealy(self, nomeEntrada):
        arquivo = open(nomeEntrada, 'r')
        self.set_nome(arquivo.readline().rstrip('\n'))

        ''' Logica para inicializar classe com valores'''
        estados = arquivo.readline().rstrip('\n').split(' ')
        self.set_estados(estados)

        alfabetoEntrada = arquivo.readline().rstrip('\n').split(' ')
        self.set_alfabetoEntrada(alfabetoEntrada)

        inicial = arquivo.readline().rstrip('\n').split(' ')
        self.set_inicial(inicial)

        finais = arquivo.readline().rstrip('\n').split(' ')
        self.set_finais(finais)

        alfabetoSaida = arquivo.readline().rstrip('\n').split(' ')
        self.set_alfabetoSaida(alfabetoSaida)

        transicao = []
        for linha in arquivo.readlines():
            linha = linha.rstrip('\n').split()
            transicao.append(linha)

        self.set_transicao(transicao)

        ''' Fechando o arquivo'''
        arquivo.close()
        return arquivo

    ''' Converte essa classe para Moore'''

    def converte_para_moore(self, moore):

        moore.set_nome('moore')

        '''Os estados devem ser atualizados posteriormente'''
        moore.set_estados(self.get_estados())
        moore.set_alfabetoEntrada(self.get_alfabetoEntrada())
        moore.set_inicial(self.get_inicial())
        moore.set_finais(self.get_finais())
        moore.set_alfabetoSaida(self.get_alfabetoSaida())


        transS = []
        for transicao in self.get_transicao():
            if (" ".join(transicao[2:])).split(' ') != ['']:
                transSaidaItem = (" ".join(transicao[2:])).split(' ')

            transS.append(transSaidaItem)
            print(transSaidaItem)
            if transSaidaItem in transS:
                transSaidaItem[0] = transSaidaItem[0] + "'"
        print(transS)

        # transSaida = []
        # for i in range(len(transS)):
        #     estado = transS[i][0]
        #     saida = transS[i][1]
        #     if [estado] in transSaida:
        #     print(estado, saida)

        return moore

    ''' Imprime seus atributos em um arquivo, formatado no padrão pedido'''

    def imprime(self, nome_arquivo):
        arquivo = open(nome_arquivo, "a")

        arquivo.write(self.get_nome() + '\n')
        arquivo.write((" ".join(self.get_estados())) + '\n')
        arquivo.write((" ".join(self.get_alfabetoEntrada())) + '\n')
        arquivo.write((" ".join(self.get_inicial())) + '\n')
        arquivo.write((" ".join(self.get_finais())) + '\n')
        arquivo.write((" ".join(self.get_alfabetoSaida())) + '\n')

        for trans in self.get_transicao():
            arquivo.write((" ".join(trans)) + '\n')

        ''' Fechando o arquivo'''
        arquivo.close()

        return 0
