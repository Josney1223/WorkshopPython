a11 = {'nome': 'a', 'nota': '8'}
a12 = {'nome': 'b', 'nota': '2'}
a13 = {'nome': 'c', 'nota': '9.5'}
a14 = {'nome': 'd', 'nota': '7'}
a15 = {'nome': 'e', 'nota': '6'}
a16 = {'nome': 'k', 'nota': '-'}

lista = [a11,a12,a13,a14,a15,a16]

p_nota = 0
s_nota = 0
t_nota = 0

p_pessoa = '0'
s_pessoa = '0'
t_pessoa = '0'

for i in lista:
    try:
        nota = float(i['nota'])
    except:
        nota = 0

    # Print inicial
    print(i['nome'], nota)
        
    # check 1 lugar    
    if nota > p_nota:
        t_nota = s_nota
        t_pessoa = s_pessoa
        s_nota = p_nota
        s_pessoa = p_pessoa
        p_nota = nota
        p_pessoa = i['nome']

    # check 2 lugar    
    elif nota > s_nota:
        t_nota = s_nota
        t_pessoa = s_pessoa
        s_nota = nota
        s_pessoa = i['nome']
        
    # check 3 lugar 
    elif nota > t_nota:
        t_nota = nota
        t_pessoa = i['nome']
    
print('Maior nota:', p_pessoa, p_nota)
print('Segunda maior nota:', s_pessoa, s_nota)
print('Terceira maior nota:', t_pessoa, t_nota)
