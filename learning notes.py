"""
operadores (dados para base de resposta)
"""
a = 10
b = 3

"""aritméticos"""
(a + b) #13
(a - b) #7
(a * b) #30
(a / b) #3.33333
(a // b) #3
(a % b) #1
(a**b) #1000

"""comparativos"""
(a == b) #False
(a != b) #True
(a > b) #True
(a < b) #False
(a >= b) #True
(a <= b) #False

"""lógicos"""
resultado_and = (a>5) and (b<5) #True
resultado_or = (a>15) or (b<5) #True
resultado_not = not (a>5) #False


"""
controles condicionais
"""
nota = 85

if nota >= 90:
    print ("Excelente")
elif nota >= 80:
    print ("Muito bom")
elif nota >= 70:
    print ("Bom")
else:
    print ("Precisa melhorar")

"""loop"""
frutas = ["maçã", "banana", "laranja"]

for frutas in frutas:
    print (frutas) #maçã, banana, laranja

"""while + break + continue + pass"""
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break
for i in range (10):
    if i%2==0:
        continue
    print (i)
for i in range (5):
    pass


"""
listas
"""
frutas = ["maçã", "banana", "laranja"]

print (frutas[0]) #maçã
print (frutas[1]) #banana
print (frutas[2]) #laranja
frutas.append("pera")
print(frutas) #maçã, banana, laranja, pera
frutas.insert(1,"uva")
print(frutas) #maçã, uva, banana, laranja, pera
frutas.remove("banana")
print(frutas) #maçã, uva, laranja, pera
fruta_removida = frutas.pop(2)
print(frutas) #maçã, uva, pera
print(fruta_removida) #laranja
frutas.sort()
print (frutas) #maçã, pera, uva
frutas.reverse
print (frutas) #uva, pera, maçã

números = [1,2,3,4,5]
quadrados = [x**2 for x in números if x%2==0]

print (quadrados) #4, 16


"""
tuplas
"""
ponto = (3,4)

print (ponto[0]) #3
print (ponto[1]) #4

minha_tupla = (1, 2, 3, 2, 4, 2)

print (minha_tupla.index(2))   # Saída: 1
print (minha_tupla.index(2, 2))   #Saída: 3
print (minha_tupla.index(2, 2, 4))   #Saída: 3


"""
dicionários
"""
pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa["nome"]) #João
print(pessoa["idade"]) #25
print(pessoa["cidade"]) #Madri

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa.keys()) #dict_keys(["nome", "idade", "cidade"])
print(pessoa.values()) #dict_values(["João", 25, "Madri"])
print(pessoa.items()) #dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])
pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  #{"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}


"""
conjuntos
"""
frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)  #{1, 2, 3, 4, 5}
intersecao = conjunto1 & conjunto2
print(intersecao)  #{3}
diferenca = conjunto1 - conjunto2
print(diferenca)  #{1, 2}
diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  #{1, 2, 4, 5}

frutas = {"maçã", "banana", "laranja"}

frutas.add("pera")
print(frutas) #"maçã", "banana", "laranja", "pera"
frutas.remove("banana")
print(frutas) #"maçã", "laranja", "pera"
frutas.discard("uva")
print(frutas) #"maçã", "laranja", "pera"
frutas.clear()
print(frutas) #set()


"""
funcoes
"""
def saudacao():
    print("Olá, mundo!")
saudacao() #"Olá, mundo!"
saudacao("João") #"Olá, João!"
saudacao("Maria") #"Olá, Maria!"

"""valores de retorno"""
def soma(a, b):
    return a + b
resultado = soma(3, 4)
print(resultado) #7

"""lambda"""
quadrado = lambda x: x ** 2
print(quadrado(5)) #25


"""variável local e global"""
def funcao():
    variavel_local = 10
    print(variavel_local) #Acesso dentro da função
variavel_global = 20
def funcao2():
    print(variavel_global) #Acesso em qualquer lugar
funcao() #10
funcao2() #20
print(variavel_global) #20
print(variavel_local) #Erro = variável não definida

"""
definido pelo usuário
"""

"""documentos/docstring"""
def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.
    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.
    Returns:
        float: A área do retângulo.
    """
    return base * altura

"""vários argumentos"""
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
print(soma_variavel(1, 2, 3)) #6
print(soma_variavel(4, 5, 6, 7)) #22

"""
exceções
"""

"""try + except"""
try:
    resultado = 10 / 0 
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")

"""finally"""
try:
    arquivo = open("arquivo.txt", "r") # Realizar operações com arquivo específico
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar arquivo sempre, mesmo com exceção

"""personalizadas"""
def funcao():
    if condicao:
        raise Exception("Descrição do erro")
try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")


""""
entrada/saída de dados
"""

"""entrada com 2 exemplos"""
nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")
print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")

idade = int(input("Insira sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

"""saída"""
nome = "Juan"
idade = 25
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

""""
arquivos
"""

"""leitura"""
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

"""escrita"""
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

"""escrita com with"""
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


""""
módulos
"""

"""importação"""
import math
resultado = math.sqrt(25)
print(resultado) #5.0

from math import sqrt
resultado = sqrt(25)
print(resultado) #5.0

"""funcao/classe"""
import random
import datetime
numero_aleatorio = random.randint(1, 10)
print(numero_aleatório)  # nº inteiro aleatório entre 1-10
data_atual = datetime.datetime.now()
print(data_atual)  #data + hora atual

"""próprio"""
#meu_modulo.py
def saudar(nome):
    print(f"Olá, {nome}!")
def calcular_soma(a, b):
    return a + b

#arquivo_importacao.py
import meu_modulo
meu_modulo.saudar("João") #"Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado) #8

"""organizacao do código"""
# operacoes.py
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b

# utilidades.py
def imprimir_mensagem(mensagem):
    print(mensagem)
def obter_nome_usuario():
    return input("Digite seu nome: ")

#importacao para programa principal
import operacoes
import utilidades

resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")
nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")

"""
pacotes
"""
#criar
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
#importar para programa
from meu_pacote import modulo1, modulo2
modulo1.funcao1()
modulo2.funcao2()
