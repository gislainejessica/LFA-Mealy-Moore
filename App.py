#!/usr/bin/python3
import sys
from Maquinas.Moore import Moore
from Maquinas.Mealy import Mealy

def main(argv):
    '''Ler arquivos da linha de comando argv e args'''
    if (len(argv) == 2):
        nomeEntrada = argv[0]
        nomeSaida = argv[1]

        ''' Criar variaveis para manipular leitura e escrita de arquivos'''
        arqEntrada = open(nomeEntrada, 'r')
        nome = arqEntrada.readline()[:-1]
        arqEntrada.close()

        arqSaida = open(nomeSaida,'w')

        if nome.lower() == 'moore':
            print('Já sei que é Moore \\0/')
            ''' Criar instância de Classe Moore '''
            moore = Moore()
            arqSaida = moore.le_moore(nomeEntrada)
            saidaConverte = moore.converte()

            moore.imprime(nomeSaida)

        elif nome.lower() == 'mealy':

            print('Já sei que é Mealy \\0/')
            ''' Instância de Classe Mealy '''
            mealy = Mealy()
            arqSaida =mealy.le_mealy(nomeEntrada)
            saidaConverte = mealy.converte()

            mealy.imprime(nomeSaida)
        else:
            print('Maquina não identificada :-( ')

        arqSaida.close()
    else:
        print('Numero de arqumentos insuficiente (Insira parametros)')

       
if __name__ == '__main__':
    main(sys.argv[1:])
