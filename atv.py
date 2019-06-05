file_notas = open('notas.txt', 'r')
a = file_notas.read()
b = a.replace('\n', ',').split(',')
file_sep = open('notas_sep.txt', 'a')

for i in range(len(b)//7):
    for u in range(i*7, i*7+7):
        y = (str(b[u])+ ' ')
        file_sep.write(y)
    print()


