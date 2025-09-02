## aula 1 paradigmas exercicio3

'''
x = float(input("Digite um numero "))

y = 7.0

def mult (a, b):
    m = a + b
    return m

print(mult(x,y))
'''

x = float(input("Digite a nota da primeira prova: "))
y = float(input("Digite a nota da segunda prova: "))

media_da_escola = 7.0

def media(a, b):
    m = (a + b)/2
    if m >= media_da_escola :
        return "O aluno passou"
    else :
        return "O aluno nao passou"

print(media(x,y))