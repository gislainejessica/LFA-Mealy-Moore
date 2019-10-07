# LFA-Mealy-Moore

Autores: **Gislaine e Ivana**

#### Pra rodar via linha de comando a aplicação
- Para rodar no terminal colocar `python3`, sequido do arquivo que precisa ser executado `App.py`, 
então colocar o nome da arquivo de entrada e o nome do arquivo de saida. 

    **Obs. :** Para rodar assim o arquivo de entrada tem que está no mesmo diretório do `App.py`. 

    Ex: 
    ```py 
    python3 App.py entrada.txt saida.txt 

- O programa pode ser executado indicando o caminho do arquivo de entrada, como indicado. Identificando caminho do arquivo, por completo, como seque:

    Ex: 
    ```py 
    python3 App.py  /home/gislaine/LFA-Mealy-Moore/Entradas/Moore/entrada1.txt  saida.txt

A saida para ambos os casos serão gerados na mesma pasta de `App.py`


*Uma descrição breve da estrutura do codigo fonte*

O Programa é composto de um Arquivo App.py que será executado com a lógica estabelecida para a leitura e processamento da Atividade, seguindo os passos de leitura de arquivo de entrada, conversão, e criação de um arquivo de saida com o resultado da conversão.

Para fazer esse processamento a funçao main() desse arquivo App.py ira utilizar as classes Mealy e Moore, onde se encontra a lógica das conversões e impressão dos atributos de cada classe. 

Os arquivos Mealy.py e Moore.py se encontram em uma pasta chamada Maquinas que será importada no arquivo de execução (App.py)
