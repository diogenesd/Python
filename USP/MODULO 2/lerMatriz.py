
def criaMatriz(l,c):
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            v = int(input("digite o valor de["+ str(i)+"]["+str(j)+"]"))
            linha.append(v)

        m.append(linha)

    return m



def lerMatriz():
    linhas = int(input("digite o numero de linhas: "))
    colunas = int(input("digite o numero de colunas: "))
    return criaMatriz(linhas, colunas)

def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz


def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim-1-i], end="  ")

