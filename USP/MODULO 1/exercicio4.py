umber = input("Digite um número inteiro: ")

hundred = int(number) // 100
ten = int(number) % 100
unitTen = ten // 10  # I just need the number of the ten

print("O dígito das dezenas é", unitTen)
