import os
import random


def Wait():
    k = input("Press enter to continue")

# Exercício filas exército
def soldiers():
    print("Esse programa foi desenvolvido com o intuito",
          " de demonstrar um posicionamento de um batalhao.", sep='\n')
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

# Exercício eleição
def election():
    expectedPeopleNumber = int(
        input("Digite o número de eleitoes esperados: "))
    colectedPeopleNumber = int(input("Digite o número de votos coletados: "))
    peopleVoteWhite = int(input("Digite o número de votos em branco: "))
    peopleVoteNull = int(input("Digite o número de votos em nulo: "))

    print("Dos", expectedPeopleNumber, "eleitores esperados,", colectedPeopleNumber,
          "eleitores compareceram, isso sendo", colectedPeopleNumber/expectedPeopleNumber*100, "% dos eleitores esperados.")
    print("Desses eleitores,", peopleVoteWhite/colectedPeopleNumber*100,
          "% votaram em branco e", peopleVoteNull/colectedPeopleNumber*100, "% votaram nulo.")

# Exercício média da nota
def media():
    P1 = int(input('Digite a nota da primeira prova: '))
    A1 = int(input('Digite a nota da primeira atividade: '))
    P2 = int(input('Digite a nota da segunda prova: '))
    A2 = int(input('Digite a nota da segunda atividade: '))
    N1 = (P1*3 + A1) / 2
    N2 = (P2*3 + A2) / 2
    NF = (N1 + N2)/2
    print("A média final dessa pessoa é:", NF)

# Conversor de data
def data():

    def StringToArray(word):
        wordArray = []
        for x in word:
            wordArray.append(x)
        return wordArray

    def Mes(mes, ano):
        if mes == 1:
            return ["Janeiro", 31]
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 400 == 0):
                return ["Fevereiro", 29, 1]
            else:
                return["Fevereiro", 28, 0]
        elif mes == 3:
            return ["Março", 31]
        elif mes == 4:
            return ["Abril", 30]
        elif mes == 5:
            return ["Maio", 31]
        elif mes == 6:
            return ["Junho", 30]
        elif mes == 7:
            return ["Julho", 31]
        elif mes == 8:
            return ["Agosto", 31]
        elif mes == 9:
            return ["Setembro", 30]
        elif mes == 10:
            return ["Outubro", 31]
        elif mes == 11:
            return ["Novembro", 30]
        elif mes == 12:
            return ["Dezembro", 31]
        else:
            return ["", 100]

    while True:
        os.system('cls')
        data = StringToArray(input("Digite uma data: <00/00/0000> "))
        dia = int(data[0]+data[1])
        mes = int(data[3]+data[4])
        ano = int(data[6] + data[7] + data[8] + data[9])

        Check = Mes(mes, ano)

        if mes > 12:
            print("Data inválida")
            Wait()
            continue
        elif dia > Check[1]:
            print("Data inválida")
            Wait()
            continue
        elif mes == 2:
            if int(Check[2]) == 0 and dia > 28:
                print("Data inválida")
                Wait()
                continue
            elif int(Check[2]) == 1 and dia > 29:
                print("Data inválida")
                Wait()
                continue

        print(dia, "de", Check[0], "de", ano)
        break

# Jogo Jokempo
def game():
    Cpontuacao = 0
    Jpontuacao = 0
    matches = 0
    while True:
        while True:
            os.system('cls')
            print("Placar: Você", Jpontuacao, "X", Cpontuacao, "Computador")
            print("1 - Pedra", "2 - Papel", "3 - Tesoura", "", sep='\n')
            x = input("Digite sua escolha: ")
            if x == "1" or x == "2" or x == "3":
                break
            else:
                print("Digite um número válido")

        y = str(random.randrange(1, 4))

        if x == y:
            print("Empate!!")

        elif (x == "1" and y == "2") or (y == "1" and x == "2"):
            if x == "1":
                print("O computador ganhou!!")
                Cpontuacao += 1
            else:
                print("Você ganhou!!")
                Jpontuacao += 1
            matches += 1

        elif (x == "2" and y == "3") or (y == "2" and x == "3"):
            if x == "2":
                print("O computador ganhou!!")
                Cpontuacao += 1
            else:
                print("Você ganhou!!")
                Jpontuacao += 1
            matches += 1

        else:
            if x == "3":
                print("O computador ganhou!!")
                Cpontuacao += 1
            else:
                print("Você ganhou!!")
                Jpontuacao += 1
            matches += 1

        if matches > 2 and Cpontuacao > Jpontuacao:
            print("O computador ganhou a melhor de 3!!!")
        elif matches > 2 and Jpontuacao > Cpontuacao:
            print("Você ganhou a melhor de 3!!!")
        Wait()

# Menu Para os executaveis
def Hub():
    while True:
        os.system('cls')
        print("1 - Soldados", "2 - Eleicoes", "3 - Média Notas",
              "4 - Conversao de data", "5 - Jokempo", "", "0 - Exit", sep="\n")
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
            data()
        elif y == '5':
            game()
        Wait()

Hub()
