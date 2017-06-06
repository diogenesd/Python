# -*- coding: utf-8 -*-
"""
@author: Andre
"""

# A. donuts
# Dado um contador (int) de donuts, retorne uma string
# na forma 'Quantidade de: <count>', aonde <count> é
# o número informado. Entretanto, se o contador for 10 ou mais,
# user a palavra 'muitos' no lugar do contador atual
# Ex.: donuts(5) retorna 'Quantidade de donuts: 5'
# e donuts(24) retorna 'Quantidade de donuts: muitos!
def donuts(count):
     if count >10 :
       return "Quantidade de: 'muitos'"
     return "Quantidade de:{}".format(count)


# B. both_ends
# Dado uma string 's', retorne a string feita os 2 primeiros
# e os 2 ultimos caracteres da string original.
# Entao, 'spring' retorna 'spng', entretanto se a string for
# menor que dois, o retorno é vazio
def both_ends(s):
  return s[:2] + s[-2:]

# C. fix_start
# Dado uma string s, retorne uma string aonde todas as
# ocorrências da primeira letra sejam alteradas por '*'
# apenas nao altere o primeiro caractere
# ex.: 'babble' retorna 'ba**le'
# Dica: s.replace(stra, strb) retorna uma versao da string s
# aonde todas as ocorrencias de sao trocadas por strb.
def fix_start(s):
  return "{}{}".format(s[0], s[1:].replace(s[0],"*"))


# D. MixUp
# Dado duas strings, retorne uma unica string com
# as strings a e b separadas por espaço, trocando os 2 primeiros
# caracteres de cada string
# Ex.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  return "{} {}".format(b[0:2]+ a[2:],a[0:2]+ b[2:])


# A. match_ends
# Dada uma lista de strings, retorne a contagem de
# strings com tamanho maior que ou igual a 2 e que
# a primeira e o ultimo caracteres sejam os mesmos

def match_ends(words):
  c = 0
  for i in words:
       if i[0] == i[-1] and len(i) > 1:
            c += 1
  return c


# B. front_x
# Dado uma lista de strings, retorne uma lista com as
# strings ordenadas, exceto o grupo de caracteres que
# que começam com a letra 'x'.
# ex.: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] resulta em
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: Voce pode fazer isso criando duas listas e ordenando-as
# antes de concatena-las

def front_x(words):
  l1 = []
  l2 = []
  for i in words:
       if i[0] == "x":
            l1.append(i)
       else:
            l2.append(i)
  return sorted(l1) + sorted(l2)


