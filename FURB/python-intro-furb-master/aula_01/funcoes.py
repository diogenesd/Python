

def funcao(*numeros, **nomeados):
    print("normais: {}".format(numeros))
    print("nomeados: {}".format(nomeados))

def funcao2(*numeros, nomeados="None"):
    print("normais: {}".format(numeros))
    print("nomeados: {}".format(nomeados))
