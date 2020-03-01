def velocidade(espaco, tempo):
    v = espaco/tempo
    return v

print(velocidade(100, 20))

def diz_oi():
    print("oi")

diz_oi()

def dados(nome, idade=None):
    print('nome: {}'.format(nome))
    if(idade is not None):
        print('idade: {}'.format(nome))
    else:
        print('idade: não informada')

dados('joao')
dados('joao', 2)

def calculadora(x, y):
    return {'soma': x+y, 'subtracao':x-y}
print(type(calculadora(1, 2)))

def velocidade_media(distancia, tempo):
    velocidade = distancia/tempo
    return velocidade
velocidade_media(100, 20)
velocidade_media(150, 22)
velocidade_media(200, 30)
velocidade_media(50, 3)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def calculadora(a, b):
    return soma(a, b), subtracao(a, b), a * b, a / b

print(calculadora(1, 1))

def teste(arg, *args):
    print('primeiro argumento normal: {}'.format(arg))
    for arg in args:
        print('outro argumento: {}'.format(arg))
teste('python', 'é', 'muito', 'legal')
lista = ['é', 'muito', 'legal']
teste('python', *lista)

def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))
minha_funcao(nome = 'caelum')
dicionario = {'nome': 'joao', 'idade': 19}
minha_funcao(**dicionario)
#A diferença é que o *args espera uma tupla de argumentos posicionais enquanto o **kwargs um dicionário com argumentos nomeados.

