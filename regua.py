def Ruler(n):
    finalSize = 2**n
    startSize = 1
    CreateRuler(startSize,finalSize, n)
    
def CreateRuler(startSize, finalSize, ordem):
    middle = (startSize + finalSize)/2
    if finalSize == 2**ordem:
        print('.')
    if ordem > 0:
        CreateRuler(startSize,middle, ordem - 1)
        DrawRuler(ordem)
        CreateRuler(middle, finalSize, ordem -1)
    if finalSize == 2**ordem:
        print('.')

def DrawRuler(size):
    print('.', end = '')
    for i in range (size):
        print('-', end = '')
    print()

Ruler(4)