matrizMxN = [[1,2],
             [1,2]]

matrizAxB = [[1,2],
             [1,2]]

# Calculo matrizF
matrizF = []
for high in range(len(matrizAxB)):
    matrizF.append([])
    for lenght in range(len(matrizMxN[0])):
        matrizF[high].append(0)
 
for m in range(len(matrizF)):
    for n in range(len(matrizF[0])):
        for i in range(len(matrizAxB)):
            matrizF[m][n] += matrizAxB[m][i] * matrizMxN[i][n]
        
for i in matrizF:
    print(i)