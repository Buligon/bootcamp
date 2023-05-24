from functools import reduce


def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc


notas = [6.4, 7.2, 5.8, 8.4]
# como o resultado de somar nota é uma função, ela é passada para o map
# executar com as notas
notas_finais = map(somar_nota(1.5), notas)

print(notas_finais)

""" for i, nota in enumerate(notas):
    notas[i] = nota + 1.5
 """"""
for i in range(len(notas)):
    notas[i] = notas[i] + 1.5
 """


def somar(a, b):
    return a+b


# if zero is ommited, start with the first two elements
total = reduce(somar, notas, 0)
