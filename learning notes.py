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

