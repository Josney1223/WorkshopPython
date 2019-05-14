import os

itemPreco = [4.00, 4.50, 5.00, 6.00, 4.00, 6.00, 4.50, 0.50]
item = ["salgado", "refrigerante", "suco", "sorvete", "cafe", "capuccino", "bolo", "dadinho"]
pessoa = []
itemDesejado = []

def Wait():
    k = input("Pressione enter para continuar")

def Menu():
    print("Menu")
    for i in range(len(item)):
        print('{:^15}'.format(item[i].capitalize()), end = '')
        print("R${:^2.2f}".format(itemPreco[i]))

def Preco(nome):
    for i in range(len(item)):
        if nome == item[i]:
            return itemPreco[i]

def PessoaFila():
    while True:
        os.system('cls')
        Menu()
        pedido = input("O que você deseja? ").lower().strip()
        if not(pedido in item):
            print("Peça algo que exista !!")
            Wait()
            continue
        else:
            itemDesejado.append(pedido)
        pessoa.append(input("Qual o seu nome? "))
        x = input("Existem mais pessoas na fila? <sim/nao> ").lower().strip()
        if x =="nao":
            ListaFinal()
        
def ListaFinal():
    os.system('cls')
    valorCaixa1 = 0
    valorCaixa2 = 0 
    half = len(pessoa)//2
    
    for i in range(half):
        print(pessoa[i], itemDesejado[i], "R$", Preco(itemDesejado[i]))
        valorCaixa1 += Preco(itemDesejado[i])
    print("O 1° caixa está com:", valorCaixa1)
    print()

    for i in range(half, len(pessoa)):
        print(pessoa[i], itemDesejado[i], "R$", Preco(itemDesejado[i]))
        valorCaixa2 += Preco(itemDesejado[i])
    print()
    print("O 2° caixa está com:", valorCaixa2)
    Wait()

PessoaFila()

