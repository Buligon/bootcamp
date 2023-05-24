class Contador:
    contador = 0  # atributo de classe

    def isnt(self):
        return 'Estou bem!'

    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    # acessa atributos de classe
    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador

    # nao acessa atributos de classe
    @staticmethod
    def mais_um(n):
        return n + 1


print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(99))
