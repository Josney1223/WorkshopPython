import os
import time
import random

def Wait():
    k = input("Pressione enter para continuar ")

## Desenhar o personagem sendo enforcado
def Draw(x):
    if x == 6:
        print(" ---|  ")
        print(" |  o  ")
        print(" | /|\ ")
        print(" | / \ ")
        print(" |     ")
        print("_|_    ")
    elif x == 5:
        print(" ---|  ")
        print(" |  o  ")
        print(" | /|\ ")
        print(" |   \ ")
        print(" |     ")
        print("_|_    ")
    elif x == 4:
        print(" ---|  ")
        print(" |  o  ")
        print(" | /|\ ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif x == 3:
        print(" ---|  ")
        print(" |  o  ")
        print(" | /|  ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif x == 2:
        print(" ---|  ")
        print(" |  o  ")
        print(" |  |  ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif x == 1:
        print(" ---|  ")
        print(" |  o  ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")
    elif x == 0:
        print(" ---|  ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print(" |     ")
        print("_|_    ")

## Transformar a palavra escolhida em uma Array       
def StringToArray(word):
    wordArray = []
    for x in word:
        wordArray.append(x)
    return wordArray

## Criar uma Array com o mesmo número de elementos que a palavra escolhida
def HiddenWord(word):
    hiddenWord = []
    for x in word:
        hiddenWord.append("-")
    return hiddenWord

## Jogo rodando
def Game():
    ## Start variáveis
    error = 0
    storage = ['abacaxi', 'morango', 'kiwi', 'manga', 'melancia']
    word = storage[random.randrange(len(storage))]
    wordArray = StringToArray(word)
    hiddenWord = HiddenWord(word)
    tries = []
    wordLenght = len(word)

    ## Main Loop
    while error < 7:
        right = False
        os.system('cls')
        Draw(error)
        
        ## Desenho da palavra escondida
        for x in hiddenWord:
            print(x, end = "")
        print()
        
        ## Desenho palavras que já foram escolhidas
        for i in tries:
            print(i, end = ", ")     
        print()

        ## Checar se existe alguma letra incógnita
        if wordLenght <=0:
            break

        ## Jogador escolhe a letra
        guess = input("Digite uma letra: ").lower().strip()

        ## Check para se a letra existe na Array da palavra escolhida
        if not(guess in tries):
            for x in range (len(word)):
                if wordArray[x] == guess:
                    hiddenWord[x] = wordArray[x]
                    right = True
                    wordLenght -= 1
        if right == False:
            error += 1
        
        ## Adicionar a letra nas tentativas
        tries.append(guess)

    ## Check final
    if error < 7:
        print("Parabéns, você ganhou!!")
        Wait()
    else: 
        print("Você perdeu!!")
        Wait()
Game()
    
    
