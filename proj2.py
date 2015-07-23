# Eduardo Janicas 78974 ; Filipa Oliveira 79197 

from random import random


#==================================================================================#
#                                 TAD COORDENADA                                   #
#==================================================================================#


def cria_coordenada(l,c):
    """CONSTRUTOR
       cria_coordenada: int x int --> coordenada
       cria_coordenada(l,c) tem como valor a coordenada correspondente a posicao (l,c)"""
    
    # l - linha, c - coluna (inteiros entre 1 e 4). Verifica a validade dos seus argumentos.
    # A representacao interna escolhida foi um tuplo, uma vez que e um tipo imutavel, adequado para 2 numeros.
    
    if not 1 <= l <= 4 or not 1 <= c <= 4 or not isinstance(l,int) or not isinstance(c,int):
        raise ValueError('cria_coordenada: argumentos invalidos')
    
    return (l,c)

    
def coordenada_linha(coord):
    """SELETOR
       coordenada_linha: coordenada --> inteiro
       coordenada_linha(coord) tem como valor a linha respetiva da coordenada"""
    
    # Selecciona o valor guardado no indice 0 do tuplo coord, correspondente a l.
    
    return coord[0]


def coordenada_coluna(coord):
    """SELETOR
       coordenada_coluna: coordenada --> inteiro
       coordenada_coluna(coord) tem como valor a coluna respetiva da coordenada"""
    
    # Selecciona o valor guardado no indice 1 do tuplo coord, correspondente a c.
    
    return coord[1]


def e_coordenada(arg):
    """RECONHECEDOR
       e_coordenada: universal --> logico
       e_coordenada(arg) tem valor verdadeiro apenas se arg e uma coordenada"""
    
    # Para que um argumento seja uma coordenada e preciso que verifique as seguintes condicoes:
    # E um tuplo com 2 entradas, em que cada uma delas (l e c) sao inteiros entre 1 e 4.
    
    return (isinstance(arg,tuple) and len(arg)==2 and isinstance(coordenada_linha(arg),int) and 
        isinstance(coordenada_coluna(arg),int) and (1 <= coordenada_linha(arg) <= 4) 
        and (1 <= coordenada_coluna(arg) <= 4))


def coordenadas_iguais(coord1,coord2):
    """TESTE
       coordenadas_iguais: coordenada x coordenada --> logico
       coordenadas_iguais(coord1,coord2) tem valor verdadeiro apenas se as coordenadas coord1 e coord2 sao iguais"""
    
    # Duas coordenadas sao iguais se cada um dos seus elementos sao iguais entre si.
    
    return (coordenada_linha(coord1) == coordenada_linha(coord2)) and (coordenada_coluna(coord1) == coordenada_coluna(coord2))


def coordenada_na_lista(coord, lista):
    """FUNCAO DE ALTO NIVEL
       coordenada_na_lista: coordenada x lista --> logico
       coordenada_na_lista(coord, lista) tem valor verdadeiro apenas se a coordenada coord existe na lista"""
    
    # Percorremos a lista e usamos a funcao que verifica se 2 coordenadas sao iguais. Casa alguma seja, a funcao devolve imediatamente
    # o valor verdadeiro
    
    for c in lista:
        if coordenadas_iguais(c, coord):
            return True
    return False    
  
  
def coordenada_to_string(coord):
    """TRANSFORMADOR DE SAIDA
    coordenada_to_string: cordenada --> string
    coordenada_to_string(coord) transfora em string do tipo <l,c> qualquer coordenada"""
    
    # Uma vez que e uma funcao de alto nivel, usamos as funcoes coordenada_linha e coordenada_coluna para devolver a coordenada
    # como uma string do tipo <l,c>
    
    return '<' + str(coordenada_linha(coord)) + ',' + str(coordenada_coluna(coord)) + '>'



#==================================================================================#
#                                 TAD TABULEIRO                                    #
#==================================================================================#

percorre_tab = range(1,5)
accoes = ('W','E','N','S')


def cria_tabuleiro():
    """CONSTRUTOR
    cria_tabuleiro: {} --> tabuleiro
    cria_tabuleiro() tem como valor um tabuleiro vazio"""
    
    # A representacao interna escolhida para o tabuleiro foi o dicionario, uma vez que e um tipo mutavel, apropriado para alterar
    # os valores das entradas, e com acesso facil a estas por nomes indexados, que irao corresponder as cordenadas como strings.
    # O tabuleiro e entao criado comecando por correr um ciclo que coloca todas as entradas entre <1,1> e <4,4> a 0, e seguidamente
    # cria a pontuacao, tambem esta a 0
    
    t = {}
    
    for l in percorre_tab:
        for c in percorre_tab:
            t[coordenada_to_string(cria_coordenada(l,c))] = 0   
    t['Pontuacao'] = 0
            
    return t


def tabuleiro_posicao(t,c):
    """SELETOR
       tabuleiro_posicao: tabuleiro x coordenada --> inteiro
       tabuleiro_posicao(t,c) tem o valor correspondente a coordenada c no tabuleiro t"""
    
    # Verifica se o segundo argumento e uma coordenada valida. Caso seja, vai buscar ao dicionario t o valor na entrada da coordenada enquanto string
    
    if not e_coordenada(c):
        raise ValueError('tabuleiro_posicao: argumentos invalidos')
    
    else:
        return t[coordenada_to_string(c)]
    

def tabuleiro_pontuacao(t):
    """SELETOR
       tabuleiro_pontuacao: tabuleiro --> int
       tabuleiro_pontuacao(t) tem como valor a pontuacao atual do tabuleiro t"""
    
    # Vai buscar ao dicionario t o valor na entrada Pontuacao
    
    return t['Pontuacao']


def tabuleiro_posicoes_vazias(t):  
    """SELETOR
       tabuleiro_posicoes_vazias: tabuleiro --> lista
       tabuleiro_posicoes_vazias(t) tem como valor uma lista contendo as coordenadas de todas as posicoes vazias do tabuleiro t"""
    
    # Comeca por criar uma lista vazia, que ira corresponder a lista que recebe todas as posicoes vazias.
    # Percorre de seguita o tabuleiro t, verificando com a funcao tabuleiro_posicao, quais as coordenadas a 0. Cada coordenada que estiver a 0
    # e colocada na lista.
    
    pos_vazias = []
    for l in percorre_tab:
        for c in percorre_tab:
            coord = cria_coordenada(l,c)
            if tabuleiro_posicao(t,coord) == 0:
                pos_vazias = pos_vazias + [coord]
    
    return pos_vazias


def tabuleiro_preenche_posicao(t,c,v):
    """MODIFICADOR
       tabuleiro_preenche_posicao: tabuleiro x coordenada x int --> tabuleiro
       tabuleiro_preenche_posicao(t,c,v) tem como valor o tabuleiro t com o valor v na posicao correspondente a coordenada c"""
    
    # Verifica se c e uma coordenada valida e v um inteiro.
    # Caso sejam, vai ao dicionario t, colocar na entrada respetiva a coordenada enquanto string o valor v introduzido
    
    if e_coordenada(c) and isinstance(v,int):
        t[coordenada_to_string(c)] = v
        return t
    
    else:
        raise ValueError("tabuleiro_preenche_posicao: argumentos invalidos")


def tabuleiro_actualiza_pontuacao(t,v):
    """MODIFICADOR
       tabuleiro_actualiza_pontuacao: tabuleiro x int --> tabuleiro
       tabuleiro_actualiza_pontuacao(t,v) tem como valor o tabuleiro t acrescentando v a respetiva pontuacao"""
    
    # Verifica que v e nao negativo e multiplo de 4. Verifica se v e um inteiro nao negativo e multiplo de 4.
    # Dado isto, vai ao dicionario t, colocar na entrada Pontuacao o valor atual da pontuacao somado com o valor v introduzido
    
    if (isinstance(v,int) and v > 0 and v % 4 == 0):
        t['Pontuacao'] = tabuleiro_pontuacao(t) + v
        return t
    
    else:
        raise ValueError("tabuleiro_actualiza_pontuacao: argumentos invalidos")
    


def tabuleiro_reduz(t,d):
    """MODIFICADOR
       tabuleiro_reduz: tabuleiro x cad. caracteres --> tabuleiro
       tabuleiro_reduz(t,d) tem como valor o tabuleiro t reduzido na direcao d incluindo a atualizacao da pontuacao"""

    # Verifica que d correspondente a uma das 4 acoes possiveis, d e uma jogada valida.
    
    if d not in accoes:
        raise ValueError('tabuleiro_reduz: argumentos invalidos')
    
    #    O Dicionario accao contem todas as variantes a usar na funcao principal dependendo do movimento da reducao.
    #    i_range corresponde a sequencia dos elementos a ser avaliada. No caso de 'W' ou 'N', e feita da primeira coordenada da linha ou coluna,
    # respectivamente, ate a ultima. Em 'E' e 'S', e feita da ultima coordenada da linha ou coluna para a primeira.
    #    i_next corresponde ao proximo elemento. Em 'W' ou 'N' e a coordenada seguinte na linha ou coluna, em 'E' e 'S' a anterior.
    #    coordenada_atual e coordenada_seguinte sao guardadas como cadeias de caracteres para serem avaliadas apenas quando lc, i e i_next estiverem definidos
    
    accao = {'W':{'i_range':range(1,4),   'i_next':1,  'coordenada_atual':'cria_coordenada(lc,i)', 'coordenada_seguinte':'cria_coordenada(lc,i+i_next)'},
             'E':{'i_range':range(4,1,-1),'i_next':-1, 'coordenada_atual':'cria_coordenada(lc,i)', 'coordenada_seguinte':'cria_coordenada(lc,i+i_next)'},
             'N':{'i_range':range(1,4),   'i_next':1,  'coordenada_atual':'cria_coordenada(i,lc)', 'coordenada_seguinte':'cria_coordenada(i+i_next,lc)'},
             'S':{'i_range':range(4,1,-1),'i_next':-1, 'coordenada_atual':'cria_coordenada(i,lc)', 'coordenada_seguinte':'cria_coordenada(i+i_next,lc)'}}
   
    i_range = accao[d]['i_range']    
    i_next = accao[d]['i_next']   
    
    #    Sao guardadas na lista coordenadas_reduzidas todas as coordenadas que ja foram reduzidas, uma vez que nao o poderao ser 2 vezes.
    #    O ciclo faz da seguinte forma:
    #    Percorrem-se todas as linhas ou colunas (lc), e, por cada uma, repete-se um conjunto de accoes (rep) ate todas as reducoes possiveis terem sido feitas
    # As accoes possiveis sao, percorrendo todas as coordenadas de uma linha ou coluna: 
    #    Caso a coordenada atual esteja vazia (=0), esta toma o valor da seguinte e a seguinte fica vazia
    #    Caso a coordenada atual nao esteja vazia e seja igual a seguinte, a atual toma a soma das 2 e a seguinte fica vazia. Esta accao so ocorre uma vez por ciclo,
    # pelas regras do jogo, pelo que a coordenada atual e a seguinte ainda nao podem ter sido reduzidas.
    

    for lc in percorre_tab:
        cordenadas_reduzidas = []
        for rep in i_range:
            for i in i_range:
                               
                coordenada_atual = eval(accao[d]['coordenada_atual'])
                coordenada_seguinte = eval(accao[d]['coordenada_seguinte']) 
            
                if  tabuleiro_posicao(t, coordenada_atual) == 0:
                    
                    tabuleiro_preenche_posicao(t, coordenada_atual, tabuleiro_posicao(t, coordenada_seguinte))
                    tabuleiro_preenche_posicao(t, coordenada_seguinte, 0)
                    
                elif  tabuleiro_posicao(t, coordenada_atual) == tabuleiro_posicao(t, coordenada_seguinte) and not coordenada_na_lista(coordenada_atual, cordenadas_reduzidas) and not coordenada_na_lista(coordenada_seguinte, cordenadas_reduzidas):
                    
                    tabuleiro_preenche_posicao(t, coordenada_atual, tabuleiro_posicao(t, coordenada_atual) + tabuleiro_posicao(t, coordenada_seguinte))
                    tabuleiro_preenche_posicao(t, coordenada_seguinte, 0)
                    cordenadas_reduzidas = cordenadas_reduzidas + [coordenada_atual]
                    tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t, coordenada_atual))
                    
                    
    return t


def e_tabuleiro(arg):
    """RECONHECEDOR
       e_tabuleiro: universal --> logico
       e_tabuleiro(t) tem valor verdadeiro apenas se arg e um tabuleiro"""
    
    #     Um argumento so e um tabuleiro se possuir as seguintes caracteristicas:
    #     E um dicionario, com 17 entradas. 16 das quais sao coordenadas, com todos os valores entre cria_coordenada(1,1) e cria_coordenada(4,4)
    # a entrada restante tem de ser a entrada 'pontuacao'.
    
    return isinstance(arg,dict) and len(arg) == 17


def tabuleiro_terminado(t):
    """RECONHECEDOR
       tabuleiro_terminado: tabuleiro --> logico
       tabuleiro_terminado(t) tem valor verdadeiro apenas se o tabuleiro t estiver terminado (cheio e sem jogadas possiveis)"""
    
   # Vamos testar se, para cada movimento possivel, o tabuleiro obtido e diferente do original. Esse teste e feito com uma copia do tabuleiro
   # para que o original nao seja modificado. Basta que algum dos resultados seja Falso para o tabuleiro nao estar terminado.
    
    for e in accoes:
        copia_tab = copia_tabuleiro(t)
        if not tabuleiros_iguais(tabuleiro_reduz(copia_tab,e),t):
            return False    
    
    return tabuleiro_posicoes_vazias(t) == []


def tabuleiros_iguais(t1,t2):
    """TESTE
       tabuleiros_iguais: tabuleiro x tabuleiro --> logico
       tabuleiros_iguais(t1,t2) tem valor verdadeiro apenas se os tabuleiros t1 e t2 tiverem a mesma configuracao e pontuacao"""
    
    # Dois tabuleiro sao iguais todas as suas entradas de coordenadas tem valores iguais e as suas pontuacoes forem iguais.
    
    for l in percorre_tab:
        for c in percorre_tab:
            coord = cria_coordenada(l,c)
            if (tabuleiro_posicao(t1,coord) != tabuleiro_posicao(t2,coord)):
                return False
    return tabuleiro_pontuacao(t1) == tabuleiro_pontuacao(t2)
     

def escreve_tabuleiro(t):
    """TRANSFORMADOR DE SAIDA
       escreve_tabuleiro: tabuleiro --> {}
       escreve_tabuleiro(t) escreve para o ecra a representacao externa de um tabuleiro de 2048"""
    
    # Verifica se t e um tabuleiro valido. Caso seja, imprime o tabuleiro linha a linha. Seguidamente, a pontuacao.
    
    if not e_tabuleiro(t):
        raise ValueError('escreve_tabuleiro: argumentos invalidos')
    
    for l in range(1,5):
        print('[',tabuleiro_posicao(t,cria_coordenada(l,1)),']','[',tabuleiro_posicao(t,cria_coordenada(l,2)),']',
              '[',tabuleiro_posicao(t,cria_coordenada(l,3)),']','[',tabuleiro_posicao(t,cria_coordenada(l,4)),'] ')
    print('Pontuacao:',tabuleiro_pontuacao(t))

    
#===============================================================================#
#                             FUNCOES ADICIONAIS                                #
#===============================================================================#


def pede_jogada():
    
    """ Pede ao utilizador para introduzir uma direcao (N, S, E ou W). Se o valor introduzido for invalido, pede novamente uma direcao """
    
    # Define o que deve ser dito ao utilizador para que este escolha uma jogada e valida-a. 
    # Caso a jogada introduzida seja invalida, o jogador e informado e e lhe pedida uma nova.
    
    d = str(input("Introduza uma jogada (N, S, E, W): "))
    
    while d not in accoes:   
        print('Jogada invalida.')
        d = str(input("Introduza uma jogada (N, S, E, W): "))
    
    return d


def copia_tabuleiro(t):
    """ Recebe como argumento t do tipo tabuleiro e devolve uma copia do mesmo """
    
    # O tabuleiro do argumento e percorrido elemento a elemento, adicionando, em cada elemento, 
    # uma copia deste ao novo tabuleiro (copia_tab), sendo por fim o copia_tab uma copia do argumento.
    
    copia_tab = {}
    
    for e in t:
        copia_tab[e] = t[e]
    
    return copia_tab
    
    
def preenche_posicao_aleatoria(t):
    """Recebe como argumento t do tipo tabuleiro e preenche uma posicao livre, escolhida aleatoriamente, com um dos numeros 2 ou 4, 
    de acordo com as probabilidades do jogo."""
    
    # A funcao random do modulo random e usada para escolher aleatoriamente uma das posicoes vazias do tabuleiro (pos_vazias) 
    # e para escolher um dos numeros 2 ou 4 segundo as probabilidades (nums_prob), 
    # preenchendo a posicao vazia escolhida com o numero escolhido.
    
    pos_vazias = tabuleiro_posicoes_vazias(t)
    
    nums_prob = (2,2,2,2,4)  # este tuplo define as probabilidades de ser escolhido 2 ou 4, sendo que a probabilidade de, 
                             # ao escolher aleatoriamente um numero deste conjunto, ser escolhido o num 2 e de 4/5 = 0.8, 
                             # e a probabilidade de escolher o num 4 e de 1/5 = 0.2 
                             
    return tabuleiro_preenche_posicao(t, pos_vazias[int(random()*len(pos_vazias))], nums_prob[int(random()*len(nums_prob))])
    
    
#===============================================================================#
#                              FUNCAO DO JOGO                                   #
#===============================================================================#


def jogo_2048():
    
    """ *Funcao do jogo* """   
    t = cria_tabuleiro()
    preenche_posicao_aleatoria(preenche_posicao_aleatoria(t)) 
    escreve_tabuleiro(t)
    
    while not tabuleiro_terminado(t):
        j = pede_jogada()
        copia_tab = copia_tabuleiro(t)
        if not tabuleiros_iguais(tabuleiro_reduz(copia_tab,j),t):
            tabuleiro_reduz(t, j)
            preenche_posicao_aleatoria(t)
        escreve_tabuleiro(t)


        
    
        
        
    
    
    