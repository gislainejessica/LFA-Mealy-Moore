#!/usr/bin/python3
import sys
import os
from Maquinas.Moore import Moore
from Maquinas.Mealy import Mealy

def main(argv):
    '''Ler arquivos da linha de comando argv e args'''
    if (len(argv) == 2):
        entrada = os.path.basename(argv[0])
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
            print(len(moore.get_transicaoSaida()[0]))
            ''' Se leitura do estado inicial não for mais que 1, verificar se não leu uma string vazia depois'''
            vazio=False
            if (len(moore.get_transicaoSaida()[0]) > 1):
                simbolo=moore.get_transicaoSaida()[0][1].split()
                if not simbolo:
                    vazio=True
            ''' Fim da verificação de simbolos vazios'''    
            if (len(moore.get_transicaoSaida()[0]) == 1 or vazio):
                mealyConvertido = moore.converte_para_mealy()
                print('Conversão realizada com sucesso')
                mealyConvertido.imprime(nomeSaida)
            else:
                print('Não é possível realizar a convesão, pois o estado inicial gera uma saída')
                moore.imprime(nomeSaida)

        elif nome.lower() == 'mealy':

            print('Já sei que é Mealy \\0/')
            ''' Instância de Classe Mealy '''
            mealy = Mealy()
            arqSaida = mealy.le_mealy(nomeEntrada)
            mooreConvertido = mealy.converte_para_moore()
            if mooreConvertido:
                print('Conversão realizada com sucesso')
                mooreConvertido.imprime(nomeSaida)

            else:
                print('Erro ao realizar conversão realizada com sucesso')
                mealy.imprime(nomeSaida)
        else:
            print('Maquina não identificada :-( ')

        arqSaida.close()
    else:
        print('Numero de arqumentos insuficiente (Insira parametros)')

       
if __name__ == '__main__':
    main(sys.argv[1:])
