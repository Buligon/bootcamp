from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7}
]

obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

# sem o casting para lista ele retorna um iterator
alunos_aprovado = list(filter(lambda aluno: aluno['nota'] >= 7, alunos))
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovado))
total = reduce(somar, notas_alunos_aprovados, 0)

print(total)
