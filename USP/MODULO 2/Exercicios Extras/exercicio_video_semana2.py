import unittest

"""
DocString for exercicio_video_semana2.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Exercicio do vídeo semana 2

"""
lista_teste = "diogenes jailton tania kiki".split()


def shorter_name(lista):
    """ Escrever uma função que recebe uma lista de Strings
            contendo nomes de pessoas como parâmentro e devolve
            o nome mais curto. A função deve ignorar espaços antes
            e depois do nome.

            Parametros: Lista de strings contendo nomes de pessoas

            Retorno: Nome mais curto da lista e formatado 'capitalize'
            """
    word = lista[0]
    shorter = len(word)
    for i in lista:
        if not isinstance(i, type(word)):
            print("não é string")
            continue

        print("tam: {}".format(len(i.strip())))
        print("tamMenor: {} ".format(shorter))
        print("menor: {}".format(word))

        if(len(i.strip()) < shorter):
            print("achou menor {}".format(i))
            word = i

    return word.capitalize()


class TestMenorNome(unittest.TestCase):

    def test_is_menor(self):
        self.assertEqual(shorter_name(lista_teste), "Kiki")
        self.assertEqual(shorter_name(lista_teste[:-1]), "Tania")

    def test_not_is_menor(self):
        self.assertNotEquals(shorter_name(lista_teste[:2]), "Kiki")
        self.assertNotEquals(shorter_name(lista_teste), "Tania")

    if __name__ == '__main__':
        unittest.main()
