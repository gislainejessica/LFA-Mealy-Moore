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

        # arqSaida = open(nomeSaida, 'w')
        # arqSaida = open(nomeSaida, 'a')
        # arqSaida.write('Criado com sucesso - Teste')

        ''' Loop para ler arquivo de entrada'''
        nome = arqEntrada.readline()[:-1]

        if nome == 'Moore':
            print('Já sei que é Moore \0/')
            ''' Criar instância de Classe Moore '''
            moore = Moore()
            while arqEntrada.readline() != '':
                linha = arqEntrada.readline()
                ''' Definir logica para inicializar classe com valores'''

            saidaConverte = moore.converte()
            # arqSaida = moore.imprime(arqSaida)
            arqSaida = moore.imprime(nomeSaida)
        elif nome == 'Mealy':
            print('Já sei que é Mealy \0/')
            ''' Criar instância de Classe Mealy '''
            mealy = Mealy()
            mealy.set_nome(nome)

            ''' Logica para inicializar classe com valores'''
            estados = arqEntrada.readline()[:-1].split(' ')
            mealy.set_estados(estados)

            alfabetoEntrada = arqEntrada.readline()[:-1].split(' ')
            mealy.set_alfabetoEntrada(alfabetoEntrada)

            inicial = arqEntrada.readline()[:-1].split(' ')
            mealy.set_inicial(inicial)

            finais = arqEntrada.readline()[:-1].split(' ')
            mealy.set_finais(finais)

            alfabetoSaida = arqEntrada.readline()[:-1].split(' ')
            mealy.set_alfabetoSaida(alfabetoSaida)

            '''Erro em logica de transicao'''
            transicao = []
            while arqEntrada.readline() != '':
                linha = arqEntrada.readline()[:-1].split(' ')
                print(linha)

                transicao.append(linha)
            mealy.set_transicao(transicao)
            saidaConverte = mealy.converte()
            # arqSaida = mealy.imprime(arqSaida)
            arqSaida = mealy.imprime(nomeSaida)
        else:
            print('Maquina não identificada :-( ')
    else:
        print('Numero de arqumentos insuficiente (Insira parametros)')
    
    ''' Fechando o arquivos'''
    arqEntrada.close()
    arqSaida.close()
       
if __name__ == '__main__':
    main(sys.argv[1:])
