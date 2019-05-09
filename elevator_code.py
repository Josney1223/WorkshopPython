import time
import os
            
## Wait
def Wait():
    k = input("Pressione enter para continuar")

## Desenhar o Elevador
def Floors(maxFloor, actualFloor, minFloor):
    for i in range(maxFloor, minFloor-1, -1):
        if (i == actualFloor):
            print("(|)", actualFloor)
        else:
            print(" | ", i)

## Desenhar os elevador em movimento para cima
def FromToUp(actualFloor, floorNumber, minFloor):
    for actualFloor in range(actualFloor, floorNumber+1):
        os.system('cls')
        Floors(maxFloor, actualFloor, minFloor)
        time.sleep(1)        
    return actualFloor

## Desenhar o elevador em movimento para baixo
def FromToDown(actualFloor, floorNumber, minFloor):
    for actualFloor in range(actualFloor, floorNumber-1, -1):
        os.system('cls')
        Floors(maxFloor, actualFloor, minFloor)
        time.sleep(1)        
    return actualFloor
        
## Loop
while True:
    # Start do loop
    os.system('cls')
    maxFloor = int(input("Quantos andares tem o predio ? "))
    while True:
        x = input("O prédio tem subsolo? <sim/nao> ").strip().lower()
        if x == "sim":
            minFloor = - int(input("Quantos andares existem abaixo da terra ? "))
            break
        elif x == "nao":
            minFloor = 0
            break

    actualFloor = 0
    end = False

    # Main Loop
    while end == False:
        floorNumber = minFloor-1
        while (floorNumber < minFloor or floorNumber > maxFloor):
            os.system('cls')
            Floors(maxFloor, actualFloor, minFloor)
            floorNumber = int(input("Digite qual andar quer visitar: "))
            if (floorNumber < minFloor or floorNumber > maxFloor):
                print("Digite um numero valido")
                Wait()
                continue

        # Check posicao do andar desejado e o atual    
        if (floorNumber > actualFloor):
            actualFloor = FromToUp(actualFloor, floorNumber, minFloor)

        elif (floorNumber < actualFloor):
            actualFloor = FromToDown(actualFloor, floorNumber, minFloor)
            
        print("Voce chegou ao seu destino!")
        Wait()

        # Check final de loop    
        x = input("Deseja ir para outro andar ? <sim/nao> ").lower().strip()
        if (x == "sim"):
            continue
        elif (x == "nao"):
            end = True

    x = input("Deseja encerrar o programa ? <sim/nao> ").lower().strip()
    if (x == "sim"):
        exit()
    elif (x == "nao"):
        continue
