arquivo = open('novo.txt', 'w')

def Invert(x):
    word = []
    invertword = ''
    
    ## Transformar a String x em uma array word
    for i in x:
        word.append(i)

    ## 'For invertido' para escrever no arquivo todas os índices da array word
    ## ao contrário no arquivo
    for i in range(len(word)-1, -1, -1):
        invertword += word[i]

    return invertword

arquivo.write(Invert('batata'))
arquivo.close()
