""" for i in range(10): # 1 to 9
    print(i)
    
for i in range(1, 11): # 1 to 10
    print(i) """

#for i in range(1, 100, 7): # 1 to 99, 7 each step
#    print(i)

#for i in range(20, 0, -3): # 1 to 99, 7 each step
#    print(i)

""" nums = [2, 4, 6, 8]

for n in nums:
	print(n, end=', ') """

""" texto = 'Python é muito massa'

for letra in texto:
	print(letra, end=' ')
 """

""" for n in {1,2,3,4,4,4}:
    print(n, end=' ')
""" 
produto = {
    'nome': 'Caneta',
    'preco': 8.8,
    'desc': 0.5
} 

""" for atributo in produto:
	print(atributo, produto[atributo])

for atributo, valor in produto.items():
	print(atributo, valor)

for  valor in produto.values():
	print(valor)
 """
for atributo in produto.keys():
	print(atributo)