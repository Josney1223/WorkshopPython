import os
import random

def Wait():
    k = input("Press enter to continue")

## Exercicios Fáceis
# Fatorial
def Fatorial(): 
    n = int(input("Digite um número: "))
    fat = 1
    while ( n > 0):
        fat *= n
        n -= 1
        
    print(fat)
                
# Triângulo
def Triangulo():
    ladoA = float(input("Digite o valor do primeiro lado: "))
    ladoB = float(input("Digite o valor do segundo lado: "))
    ladoC = float(input("Digite o valor do terceiro lado: "))
            
    def verificarSoma(A, B, C):
        y = 0
        if (A > B + C):
            x = ("False")
            y = 1
        elif (B > A + C):
            x = ("False")
            y = 1
        elif (C > A + B):
            x = ("False")
            y = 1
        else:
            x = ("True")
        print("É um triângulo: " + x)
        return y
                
    def equilatero(A, B, C):
        if (A == B and B == C):
            print("É equilátero? True")
        else:
            print("É equilátero? False")
                
    def isoceles(A, B, C):
        if (A == B or B == C):
            print("É isóceles? True")
        else:
            print("É isóceles? False")
                
    def escaleno(A, B, C):
        if (A != B and B != C):
            print("É escaleno? True")
        else:
            print("É escaleno? False")

    tri = verificarSoma(ladoA, ladoB, ladoC)
    if (tri != 1):
        equilatero(ladoA, ladoB, ladoC)
        isoceles(ladoA, ladoB, ladoC)
        escaleno(ladoA, ladoB, ladoC)

# Exercício eleição
def Election():
    expectedPeopleNumber = int(input("Digite o número de eleitoes esperados: "))
    colectedPeopleNumber = int(input("Digite o número de votos coletados: "))
    peopleVoteWhite = int(input("Digite o número de votos em branco: "))
    peopleVoteNull = int(input("Digite o número de votos em nulo: "))

    print("Dos", expectedPeopleNumber, "eleitores esperados,", colectedPeopleNumber,
          "eleitores compareceram, isso sendo", colectedPeopleNumber/expectedPeopleNumber*100, "% dos eleitores esperados.")
    print("Desses eleitores,", peopleVoteWhite/colectedPeopleNumber*100,
          "% votaram em branco e", peopleVoteNull/colectedPeopleNumber*100, "% votaram nulo.")

# Exercício média da nota
def Media():
    P1 = int(input('Digite a nota da primeira prova: '))
    A1 = int(input('Digite a nota da primeira atividade: '))
    P2 = int(input('Digite a nota da segunda prova: '))
    A2 = int(input('Digite a nota da segunda atividade: '))
    N1 = (P1 + A1*3) / 4
    N2 = (P2 + A2*3) / 4
    NF = (N1 + N2) / 2
    print("A média final dessa pessoa é:", NF)

# Mínimo multiplo comum
def Mdc():
    valor = int(input("Digite um número: "))
    divisor = int(input("Digite o valor do divisor: "))
    resto = 1
    while (resto != 0):
        resto = valor % divisor
        if (resto == 0):
            print("MDC = " + str(divisor))
        else:
            valor = divisor
            divisor = resto

# Operações com números primos
def Prime():
    def Primo(x):
        y = 1
        divisores = 0
        while(y <= x):
            if (x % y == 0):
                divisores += 1
                y += 1
            else:
                y += 1
        if (divisores == 2):
            return True
        else:
            return False

    def Divisivel(x,y):
        if (x % y == 0):
            return True
        else:
            return False
        
    def Primos(n):
        x = 1
        while (x <= n):        
            if Primo(x):
                print(x, end = ', ')
            x += 1
                    
    def info():
        print(" ")
        print("------------------/------------------")
        print("0. Exit")
        print("1. Número Primo")
        print("2. Divisibilidade de X por Y")
        print("3. Todos os números primos até N", end = '\n\n')
        
    while True:
        info()
        operacao = int(input("Digite a operação que deseja realizar: "))
        if (operacao == 0):
            exit()
        elif (operacao == 1):
            x = int(input("Digite o número: "))
            if Primo(x):
                print("É um número primo")
            else:
                print("Não é número primo")
        elif (operacao == 2):
            x = int(input("Digite o valor de X: "))
            y = int(input("Digite o valor de Y: "))
            if Divisivel(x,y):
                print(str(x) + " é divisível por " + str(y))
            else:
                print(str(x) + " não é divisível por " + str(y))
        elif (operacao == 3):
            n = int(input("Digite o valor de n: "))
            Primos(n)

## Exercicios Dificeis
# Leilão
def Auction():
    lances = []
    person = []
    maxNumber = 0
        
    while True:
        x = int(input("Digite o seu lance: "))
        lances.append(x)
        z = input("Quem fez esse lance? ")
        person.append(z)
        y = input("Acabaram os lances? <sim/nao> ").lower().strip()
        if y == 'sim':
            break
        else:
            continue

    while True:
        for x in range (len(lances)):
            if maxNumber < int(lances[x]):
                maxNumber = int(lances[x])
                personMaxNumber = person[x]
        print("O maior lance é:", maxNumber, "de", personMaxNumber)
        break

# Filas exército
def Soldiers():
    print("Esse programa foi desenvolvido com o intuito",
          " de demonstrar um posicionamento de um batalhao.", sep='\n')
    x = int(input("Digite um número de soldados: "))
    filas = 0
    n = 0

    while x > 0:
        n += 1
        x -= n
        filas += 1

    print("O número de fileiras formadas foi", filas)

    if x < 0:
        print("e restaram", x + n, "soldados na última fileira.")

# Fibonacci
def Fibonacci():
    n = int(input("Digite até que número deseja chegar na sequência Fibonacci: "))
    for x in range(0, n):
        if x == 0:
            y = 0
            print("fib(" + str(x)+") =", y)
            y2 = y
        elif x == 1:
            y += 1
            print("fib(" + str(x)+") =", y)
            y1 = y
        else:
            print("fib(" + str(x)+") =", y)
            y2 = y1
            y1 = y
            y = y1 + y2

# Conversor de data
def Data():

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
def Jokempo():
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
            break
        elif matches > 2 and Jpontuacao > Cpontuacao:
            print("Você ganhou a melhor de 3!!!")
            break
        Wait()

# Menu Para os executaveis
def Hub():
    while True:
        os.system('cls')
        print("1 - Exercicios Dificeis", "2 - Exercicios Faceis", "", "0 - Exit", sep="\n")
        x = input("Digite sua escolha: ").strip()

        if x == '0':
            exit()

        elif x == '1':
            while True:
                os.system('cls')
                print("1 - Leilão", "2 - Soldados", "3 - Fibonacci", "4 - Conversao de data", "5 - Jokempo", "", "0 - Exit", sep="\n")
                y = input("Digite sua escolha: ").strip()
                if y == "0":
                    exit()
                elif y == '1':
                    Auction()
                elif y == '2':
                    Soldiers()
                elif y == '3':
                    Fibonacci()
                elif y == '4':
                    Data()
                elif y == '5':
                    Jokempo()

                Wait()

        elif x == '2':
            while True:
                os.system('cls')
                print("1 - Fatorial", "2 - Triângulo", "3 - Eleição", "4 - Média Final", "5 - Mínimo Multiplo Comum", "6 - Números Primos", "0 - Exit", sep="\n")
                y = input("Digite sua escolha: ").strip()
                if y == "0":
                    exit()
                elif y == '1':
                    Fatorial()
                elif y == '2':
                    Triangulo()
                elif y == '3':
                    Election()
                elif y == '4':
                    Media()
                elif y == '5':
                    Mdc()
                elif y == '6':
                    Prime()
                Wait()

Hub()