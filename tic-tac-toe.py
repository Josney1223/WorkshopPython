import os

board = {'top_L': '1', 'top_M': '2', 'top_R': '3',
         'mid_L': '4', 'mid_M': '5', 'mid_R': '6',
         'bot_L': '7', 'bot_M': '8', 'bot_R': '9'}

def Wait():
    k = input("Pressione enter para continuar")
    
def Print():
    print(board['top_L'],'|', board['top_M'], '|', board['top_R'])
    print('--+---+--')
    print(board['mid_L'],'|', board['mid_M'], '|', board['mid_R'])
    print('--+---+--')
    print(board['bot_L'],'|', board['bot_M'], '|', board['bot_R'])

yAxis = ['L','M','R']
xAxis = ['top','mid','bot']

turn = 'X'
for i in range(9):
    begin = False
    x = input('Escolha sua jogada ' + turn + ' : ')
    for y in board:
        if board[y] == x:
            board[y] = turn
        elif board[y] == 'X':
            print('Jogada inválida !!')
            begin = True
        elif board[y] == 'O':
            print('Jogada inválida !!')
            begin = True

    if begin == True:
        continue

    Print()    
    # Check vitória
    for u in yAxis:
        if board['top_'+u] == turn and board['mid_'+u] == turn and board['bot_'+u] == turn:
            print(' O jogador do', turn, 'ganhou !!!')
            Wait()
    for u in xAxis:
        if board[u+'_L'] == turn and board[u+'_M'] == turn and board[u+'_R'] == turn:
            print(' O jogador do', turn, 'ganhou !!!')
            Wait()
    if (board['top_L'] == turn and board['mid_M'] == turn and board['bot_R'] == turn) or (board['top_R'] == turn and board['mid_M'] == turn and board['bot_L'] == turn):
        print(' O jogador do', turn, 'ganhou !!!')
        Wait()
        
    # Trocar turno
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    os.system('cls')
    Print()
