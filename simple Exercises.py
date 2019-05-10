import os

def Wait():
    k = input("Press enter to continue")

## Atividade
def soldiers():
    print("Esse programa foi desenvolvido com o intuito", " de demonstrar um posicionamento de um batalhao.", sep = '\n')
    x = int(input("Digite um número de soldados: "))
    filas = 0
    n = 1

    while x > 0:
        x -= n
        filas += 1
        n += 1

    print("O número de fileiras formadas foi", filas)

    if x < 0:
        x -= -(n-1)
        print("e restaram", x, "soldados na última fileira.")

def election():
    expectedPeopleNumber = int(input("Digite o número de eleitoes esperados: "))
    colectedPeopleNumber = int(input("Digite o número de votos coletados: "))
    peopleVoteWhite = int(input("Digite o número de votos em branco: "))
    peopleVoteNull = int(input("Digite o número de votos em nulo: "))

    print("Dos", expectedPeopleNumber, "eleitores esperados,", colectedPeopleNumber, "eleitores compareceram, isso sendo", colectedPeopleNumber/expectedPeopleNumber*100,"% dos eleitores esperados.")
    print("Desses eleitores,", peopleVoteWhite/colectedPeopleNumber*100, "% votaram em branco e", peopleVoteNull/colectedPeopleNumber*100, "% votaram nulo.")

def media():
    for i in range(50):
        P1 = int(input('Digite a nota da primeira prova: '))
        A1 = int(input('Digite a nota da primeira atividade: '))
        P2 = int(input('Digite a nota da segunda prova: '))
        A2 = int(input('Digite a nota da segunda atividade: '))
        N1 = (P1*3 + A1) / 2
        N2 = (P2*3 + A2) / 2
        NF = (N1 + N2)/2
        print("A média final dessa pessoa é:", NF)
        Wait()

##def convert():

##def game():

## Atividade +1
# def soldiersPrint():

#     def Draw(Height, Width):
#         Matrix = [[0 for x in range(Width)] for y in range(Height-1)]
#         return Matrix

#     print("Esse programa foi desenvolvido com o intuito", " de demonstrar um posicionamento de um batalhao.", sep = '\n')
#     x = int(input("Digite um número de soldados: "))
#     filas = 0
#     n = 1

#     while x > 0:
#         x -= n
#         filas += 1
#         n += 1

#     y = Draw(n, filas)
#     print(y)
#     print("O número de fileiras formadas foi", filas)

#     if x < 0:
#         x -= -(n-1)
#         print("e restaram", x, "soldados na última fileira.")

def Hub():
    #print("1 - Atividade", "2 - Atividade+", sep = "\n")
    #print()
    #x = int(input("Digite a sua dificuldade: "))
    x = 1
    if x == 1:
        while True:
            os.system('cls')
            print("1 - Soldados", "2 - Eleicoes", "3 - Média Notas", "4 - Conversao de data", "5 - Jokempo", "", "0 - Exit", sep = "\n")
            y = input("Digite sua escolha: ").strip()
            if y == "0":
                exit()
            elif y == '1':
                soldiers()
            elif y == '2':
                election()
            elif y == '3':
                media()
            elif y == '4':
                convert()
            elif y == '5':
                game()
            Wait()
        
    #elif x == 2:

Hub()