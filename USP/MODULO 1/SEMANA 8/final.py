import re
from decimal import *

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def lista_frases(sentencas):
    frases = []
    for i in sentencas:
        frases += separa_frases(i)
    return frases

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def lista_palavras(frases):
    palavras = []
    for i in frases:
        palavras += separa_palavras(i)
    return palavras

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    #as_a = [x, x, x, x, x, x] || as_b = [y, y, y, y, y, y]

    tam = len(as_a)
    soma = 0

    for i in range(tam):
        a = as_a[i]
        b = as_b[i]
        if( b > a ):
            soma += (b - a)
        else:
            soma += (a - b)

    similaridade = soma / tam

    return round(similaridade, 2)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    a = tamanho_medio_palavras(lista_frases(separa_sentencas(texto)))
    b = r_type_token(texto)
    c = r_hapax_legomana(texto)
    d = tamanho_medio_sentencas(texto)
    e = complexidade(separa_sentencas(texto))
    f = tamanho_medio_frase(lista_frases(separa_sentencas(texto)))
  
    return [a, b, c, d, e, f]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma
    lista de textos e deve devolver o numero (0 a n-1)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    r = []
    tam = len(textos)
    for i in textos:
        s = compara_assinatura(calcula_assinatura(i),ass_cp)
        r.append(s)

    print("O autor do texto", r.index(min(r)),"está infectado com COH-PIAH")
    return r.index(min(r))

def tamanho_medio_palavras(frases):

    p =[]
    for i in frases:
        p += separa_palavras(i)    

    s = 0
    for i in p:
        s += len(i)

    t = len(p)
    
    return s / t


def tamanho_medio_sentencas(texto):
    sentencas = separa_sentencas(texto)
    t = len(sentencas)
    
    s = 0
    for i in sentencas:
        s += len(i)
    return s / t


def type_token(palavras):
    s = n_palavras_diferentes(palavras)
    t = len(palavras)
    return s / t
    
def hapax_legomana(palavras):
    s = n_palavras_unicas(palavras)
    t = len(palavras)
    return s / t


def complexidade(sentencas):
    f = []
    for i in sentencas:
        f += separa_frases(i)

    tf = len(f)
    ts = len(sentencas)
    return  tf / ts
    
def tamanho_medio_frase(frases):
    s = 0
    for i in frases:
        s += len(i)

    tf = len(frases)
    return s / tf


def grau(t1,t2):
    a = tamanho_medio_palavras(t1)
    b = r_type_token(t1)
    c = r_hapax_legomana(t1)
    d = tamanho_medio_palavras(t1)
    e = complexidade(t1)
    f = tamanho_medio_frase(t1)
    fa = abs(a) + abs(b) + abs(c) + abs(d) + abs(e) + abs(f)

    a = tamanho_medio_palavras(t2)
    b = r_type_token(t2)
    c = r_hapax_legomana(t2)
    d = tamanho_medio_palavras(t2)
    e = complexidade(t2)
    f = tamanho_medio_frase(t2)
    fb = abs(a) + abs(b) + abs(c) + abs(d) + abs(e) + abs(f)
    
    return (fa - fb) / 6

def soma_palavras(palavras):
    s = 0
    t = len(palavras)
    for i in range(t):
        for j in palavras[i]:
            s +=1
    return s
    
def r_type_token(texto):
    ls = separa_sentencas(texto)
    lf = lista_frases(ls)
    lp = lista_palavras(lf)
    return type_token(lp)
    
def r_hapax_legomana(texto):
    ls = separa_sentencas(texto)
    lf = lista_frases(ls)
    lp = lista_palavras(lf)
    return hapax_legomana(lp)

def somatorio(as_a, as_b):
    soma = (as_a[0]-as_b[0])+(as_a[1]-as_b[1])+(as_a[2]-as_b[2])+(as_a[3]-as_b[3])+(as_a[4]-as_b[4])+(as_a[5]-as_b[5])
    return soma

def sep_texto_in_frases(texto):
    s = separa_sentencas(texto)
    f = []
    for i in s:
      f.append(separa_frases(i))
    return f

##### TESTES ################################################

# FUNCIONA
def testa_tamanho_medio_palavras():
    texto = "O gato caçava o rato." # 16 / 5 = 3,2
    texto2 = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
    f = lista_frases(separa_sentencas(texto2))
    tam = tamanho_medio_palavras(f) # texto2 =  tam. médio palavra esperado: 5.189;
    print(tam)

# FUNCIONA
def testa_r_type_token():
    texto = "O gato caçava o rato" # relação type-token esperado:0.8
    texto2 = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
    rel = r_type_token(texto2)  # relação type-token esperado: 0.743
    print(rel)

# FUNCIONA
def testa_r_hapax_legomana():
    texto = "O gato caçava o rato."
    rel = r_hapax_legomana(texto)
    print(rel)

# FUNCIONA
def testa_tamanho_medio_sentencas():
    texto = "O gato caçava o rato. O gato caçava o rato"
    tam = tamanho_medio_sentencas(texto)
    print(tam)

# FUNCIONA
def testa_complexidade():
    texto = "O gato caçava o rato,O gato caçava o rato,O gato caçava o rato.O gato caçava o rato"
    s = separa_sentencas(texto)
    comp = complexidade(s)
    print(comp)
    
# FUNCIONA
def testa_tamanho_medio_frase():
    texto = "O gato caçava o rato,O gato caçava o rato.O gato caçava o rato"
    f = lista_frases(separa_sentencas(texto))
    tam = tamanho_medio_frase(f)
    print(tam)

# FUNCIONA
def testa_calcula_assinatura():
    texto = "O gato caçava o rato"
    return calcula_assinatura(texto)

# FUNCIONA
def testa_compara_assinatura():
    
    #ass1 = [4.34, 0.05, 0.02, 12.81, 2.16, 0.0],
    #ass2 = [3.96, 0.05, 0.02, 22.22, 3.41, 0.0])
    #Esperado: 1.84
    
    ass1 = [4.34, 0.05, 0.02, 12.81, 2.16, 0.0]
    ass2 = [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]
    s = compara_assinatura(ass1,ass2) 
    print(s)

def testa_avalia_textos():
    ass_cp = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
    t1 = "Navegadores antigos tinham uma frase gloriosa:\"Navegar é preciso; viver não é preciso\". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
    t2 = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
    t3 = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
    #return avalia_textos([t1,t2,t2],ass_cp)

    Textos = ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.', 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.', 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']
    Assinatura = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
    # Esperado: 1;
    return avalia_textos(Textos,Assinatura)
    
