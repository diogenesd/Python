
n = 0
m = 0
removidas = 0

def computador_escolhe_jogada(n, m):
        i = 1
        r = m
        while i <= m:
                if multiplo(n-i,m):
                        r = i
                i += 1
        return r
                              
                              
def usuario_escolhe_jogada(n, m):
        remove = -1
        while remove == -1:
                print("")
                remove = int(input("Quantas peças você vai tirar? "))
                if remove <= m and remove > 0:
                        return remove
                else:
                        print("")
                        print("Oops! Jogada inválida! Tente de novo.")
                        remove = -1

		
def multiplo(n,m):
	if n % (m + 1) == 0:
		return True
	return False

def inicia():
       print("")
       p = int(input("Quantas peças? "))
       while p <= 0:
               print("Quantidade inválida, digite novamente")
               p = int(input("Quantas peças? "))

       r = int(input("Limite de peças por jogada? "))
       while r <= 0:
               print("Quantidade limite inválida, digite novamente")
               r = int(input("Quantas peças você vai tirar? "))

       global n
       n = p
       global m
       m = r
		       

def partida():
        inicia()
        vezUSER = multiplo(n,m)

        if vezUSER == True:
                print("")
                print("Você começa")
                remove_peca(usuario_escolhe_jogada(n,m))
        else:
                print("")
                print("Computador começa!")
                remove_peca(computador_escolhe_jogada(n,m))

        statusJogo(vezUSER)

        while n != 0:
                vezUSER = not vezUSER
                
                if vezUSER == True:
                        remove_peca(usuario_escolhe_jogada(n,m))
                else:
                        remove_peca(computador_escolhe_jogada(n,m))

                statusJogo(vezUSER)
                
        return fimJogo(vezUSER)
	
def fimJogo(vez):
        print("")
        if vez == True:
                print("Você ganhou!")
                return "USER"
        else:
                print("O computador ganhou!")
                return "PC"
        
def statusJogo(vez):
	print("")
	global removidas
	global n
	if vez == True:
		print("Você tirou",removidas,"peça(s)!")
	else:
		print("O computador tirou",removidas,"peça(s)!")
	if(n == 1):
		print("Agora resta apenas uma peça no tabuleiro.")
	else:
		print("Agora restam",n,"peça(s) no tabuleiro.")

def remove_peca(qtd):
        global n
        n -= qtd
        global removidas
        removidas = qtd
	
def campeonato():
	i = 1
	placar_user = 0
	placar_pc = 0
	while i <= 3:
		print("")
		print("**** Rodada",i,"****")
		vencedor = partida()
		if vencedor == "PC":
			placar_pc += 1
		else:
			placar_user += 1
		i +=1

	print("")
	print("**** Final do campeonato! ****")
	print("")
	print("Placar: Você",placar_user,"X",placar_pc,"Computador")

	
def main():
        print("")
        print("Bem-vindo ao jogo do NIM! Escolha:")
        escolha = -1
        while escolha == -1:
                print("")
                print("1 - para jogar uma partida isolada")
                escolha = int(input("2 - para jogar um campeonato "))
                if escolha == 1:
                        print("")
                        print("Voce escolheu uma partida isolada!")
                        print("")
                        print("**** Partida Única ****")
                        partida()
                        print("")
                        print("**** Fim da partida! ****")      
                elif escolha == 2:
                        print("")
                        print("Voce escolheu um campeonato!")
                        campeonato()
                else:
                        print("")
                        print("Digite uma opção válida!")
                        escolha = -1

def test_computador_escolhe_jogada():
        assert computador_escolhe_jogada(6, 2) == 2
        assert computador_escolhe_jogada(15, 4) == 4
        
        
main()
