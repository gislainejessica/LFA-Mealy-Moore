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
        arqSaida = open(nomeSaida, 'w')
        arqSaida.write('Criado com sucesso - Teste')

        ''' Loop para ler arquivo de entrada'''
        nome = arqEntrada.readline()
    
        if nome == 'Moore':
            print('Já sei que é Moore \0/')
            ''' Criar instância de Classe Moore '''
            moore = Moore()
            while arqEntrada.readline() != '':
                linha = arqEntrada.readline()
                ''' Definir logica para inicializar classe com valores'''
            saidaConverte = moore.converte()
            arqSaida = moore.imprime(arqSaida)
        elif nome == 'Mealy':
            print('Já sei que é Mealy \0/')
            ''' Criar instância de Classe Mealy '''
            mealy = Mealy()
            while arqEntrada.readline() != '':
                linha = arqEntrada.readline()
                ''' Definir logica para inicializar classe com valores'''
            saidaConverte = mealy.converte()
            arqSaida = mealy.imprime(arqSaida)
        else:
            print('Maquina não identificada :-( ')
    else:
        print('Numero de arqumentos insuficiente (Insira parametros)')
    
    ''' Fechando o arquivos'''
    arqEntrada.close()
    arqSaida.close()
       
if __name__ == '__main__':
    main(sys.argv[1:])
