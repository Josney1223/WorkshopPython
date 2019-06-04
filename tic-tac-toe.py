import os

# Inicialização
yAxis = ['L','M','R']
xAxis = ['top','mid','bot']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
end = False
turn = 'X'
contdown = 0
board = {'top_L': 1, 'top_M': 2, 'top_R': 3,
         'mid_L': 4, 'mid_M': 5, 'mid_R': 6,
         'bot_L': 7, 'bot_M': 8, 'bot_R': 9}

def Wait():
    k = input("Pressione enter para continuar")

# Desenhar o tabuleiro    
def Print():
    os.system('cls')
    print(board['top_L'],'|', board['top_M'], '|', board['top_R'])
    print('--+---+--')
    print(board['mid_L'],'|', board['mid_M'], '|', board['mid_R'])
    print('--+---+--')
    print(board['bot_L'],'|', board['bot_M'], '|', board['bot_R'])

## Main Loop
while True:
    begin = False
    Print()
    x = int(input('Escolha sua jogada ' + turn + ' : '))

    # Check se é uma jogada válida
    if not(x in numbers):
        print('Jogada inválida')
        Wait()
        continue
    else:
        for y in board:
            if board[y] == x:
                board[y] = turn
                numbers.remove(x)

    # Check vitória
    Print()
    for u in yAxis:
        if board['top_'+u] == turn and board['mid_'+u] == turn and board['bot_'+u] == turn:
            end = True
    for u in xAxis:
        if board[u+'_L'] == turn and board[u+'_M'] == turn and board[u+'_R'] == turn:
            end = True
    if (board['top_L'] == turn and board['mid_M'] == turn and board['bot_R'] == turn) or (board['top_R'] == turn and board['mid_M'] == turn and board['bot_L'] == turn):
        end = True

    ## Condições de témino
    # Vitória
    if end == True:
        print('O jogador do', turn, 'ganhou !!!')
        Wait()
        exit()

    # Deu velha
    elif contdown == 8:
        print('Deu velha !!!')
        Wait()
        exit()

    ## Trocar turno
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        contdown += 1
            
