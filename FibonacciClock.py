import os
from colorama import init
init()
import time

def FibonacciClock(hora, minutos):
    while True:
        RealH = hora
        RealM = minutos
        pontos = [5, 3, 2, 1, 1]
        pA = []
        pVM = []
        pV = []
        A1 = False
        A2 = False
        A3 = False
        A4 = False
        A5 = False
        A1C = '\x1b[1;37;40m'
        A2C = '\x1b[1;37;40m'
        A3C = '\x1b[1;37;40m'
        A4C = '\x1b[1;37;40m'
        A5C = '\x1b[1;37;40m'
        Azul = 0
        Vermelho = 0
        Verde = 0

        if hora >= (minutos/5):
            hora -= minutos/5
            Azul = minutos/5
            minutos = 0
        else:
            minutos -= hora*5
            Azul = hora
            hora = 0

        if hora > 0:
            Vermelho = hora
            Verde = 0
        elif minutos > 0:
            Verde = minutos/5
            Vermelho = 0

        for x in pontos:
            if Azul >= x:
                pA.append(x)
                Azul -= x
            elif Vermelho >= x:
                pVM.append(x)
                Vermelho -= x
            elif Verde >= x:
                pV.append(x)
                Verde -= x

        for k in pA:
            if k == 5 and A1 == False:
                A1 = True
                A1C = '\x1b[1;34;40m'
            elif k == 3 and A2 == False:
                A2 = True
                A2C = '\x1b[1;34;40m'
            elif k == 2 and A3 == False:
                A3 = True
                A3C = '\x1b[1;34;40m'
            elif k == 1 and A4 == False:
                A4 = True
                A4C = '\x1b[1;34;40m'
            elif k == 1 and A5 == False:
                A5 = True
                A5C = '\x1b[1;34;40m'

        for k in pVM:
            if k == 5 and A1 == False:
                A1 = True
                A1C = '\x1b[1;31;40m'
            elif k == 3 and A2 == False:
                A2 = True
                A2C = '\x1b[1;31;40m'
            elif k == 2 and A3 == False:
                A3 = True
                A3C = '\x1b[1;31;40m'
            elif k == 1 and A4 == False:
                A4 = True
                A4C = '\x1b[1;31;40m'
            elif k == 1 and A5 == False:
                A5 = True
                A5C = '\x1b[1;31;40m'

        for k in pV:
            if k == 5 and A1 == False:
                A1 = True
                A1C = '\x1b[1;32;40m'
            elif k == 3 and A2 == False:
                A2 = True
                A2C = '\x1b[1;32;40m'
            elif k == 2 and A3 == False:
                A3 = True
                A3C = '\x1b[1;32;40m'
            elif k == 1 and A4 == False:
                A4 = True
                A4C = '\x1b[1;32;40m'
            elif k == 1 and A5 == False:
                A5 = True
                A5C = '\x1b[1;32;40m'

        os.system('cls')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A2C+'OOOOOOOOOOOOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A2C+'OOOOOOOOOOOOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A2C+'OOOOOOOOOOOOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A2C+'OOOOOOOOOOOOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A2C+'OOOOOOOOOOOOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A2C+'OOOOOOOOOOOOOOOOOOOO')

        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A3C +'OOOOOOOOOO', end = '')
        print(A4C+'OOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A3C +'OOOOOOOOOO', end = '')
        print(A4C+'OOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A3C +'OOOOOOOOOO', end = '')
        print(A4C+'OOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A3C +'OOOOOOOOOO', end = '')
        print(A5C+'OOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A3C +'OOOOOOOOOO', end = '')
        print(A5C+'OOOOOOOOOO')
        print(A1C+'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO', end = '')
        print(A3C +'OOOOOOOOOO', end = '')
        print(A5C+'OOOOOOOOOO')

        for i in range (5):
            for y in range(60):
                time.sleep(1)
        
        RealM += 5
        if RealM == 60:
            RealM = 0
            RealH += 1
        hora = RealH
        minutos = RealM

FibonacciClock(3, 0)
