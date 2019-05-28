matrizMxN = [[1,2,3],
             [1,2,3]]

matrizAxB = [[1,2],
             [1,2],
             [1,2]]

# Calculo matrizF
matrizF = []
for high in range(len(matrizMxN)):
    matrizF.append([])
    for lenght in range(len(matrizAxB[0])):
        matrizF[high].append(0)
 
for m in range(len(matrizF)):
    for n in range(len(matrizF[0])):
        for i in range(len(matrizMxN[0])):
            matrizF[m][n] += matrizAxB[i][n] * matrizMxN[m][i]
        
for i in matrizF:
    print(i)
