
class Moore(object):
    ''' Receber paramentros para inicializar a classes com os valores lidos
        Por enquanto, a classe tá inicializando com valores default
    '''
    def __init__(self):
        self.nome = 'Moore'
        self.estados = ['s*', 's1', 's2']
        self.alfabetoEntrada = ['a','b','c']
        self.inicial = 's*'
        self.finais = ['--']
        self.alfabetoSaida = ['T', 'F', 'O']
        ''' Função de Transição... Thinking '''
        
    ''' Converte essa classe para Mealy'''
    def converte(self):
        return 

    ''' Imprime seus atributos em um arquivo, formatado no padrão pedido'''
    def imprime(self, arquivo):
        return arquivo