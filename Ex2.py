# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
def possui_letra(s):
    #Coloca a entrada do usuário em minusculo e conta a quantidade de letras 'a'
    return s.lower().count('a')

# Entrada do usuário
s = input("Digite uma string para verificar: ")

# Verificação da função possui_letra
if possui_letra(s):
    print(f"A string {s} contém {possui_letra(s)} letra(s) 'a'.")
else:
    print(f"A string {s} não contém a letra 'a'.")