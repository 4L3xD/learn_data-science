"""class a():
    def __init__(self, nome):
        print("Aaaaa!")
        self.nome = nome

class b(a):
    def __init__(self, nome):
        print("Bbbbb!")
        super().__init__(nome)

#c = a("Teste")
d = b("Teste") # super().__init__(nome)
print(d.nome)"""

"""class estudante():
    def __init__(self, nome, num_doc, nascimento, nacionalidade, residencia):
        self.nome = nome
        self.num_doc = num_doc
        self.nascimento = nascimento
        self.nacionalidade = nacionalidade
        self.residencia = residencia

class perfil(estudante):
    def __init__(self, nome, n_doc, nascimento, nacionalidade, residencia):
        super().__init__(nome, n_doc, nascimento, nacionalidade, residencia)

cadastro = perfil("Ale", 1234, "02/01/1995", "brasileira", "Brasil")
print(cadastro.num_doc)"""

"""class Animal():
    def says(self):
        return "I speak!"

class Donkey(Animal):        
    def says(self):
        return "Hee-haw!"
class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Mule(Donkey, Horse):
    pass

print(Mule.mro()) #[<class '__main__.Mule'>, <class '__main__.Donkey'>, <class '__main__.Horse'>, <class 'object'>]
mule = Mule()
print(mule.says())"""

"""class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass

t = Thing()
t.name = "Babuíno"
t.feature = "POO"
t.dump()
print(t)"""

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    #@property
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    #@name.setter
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

don = Duck("Donald")
print(don.get_name())
don.set_name('Donna')
print(don.get_name())

##################### outras maneiras de acesso
#linha 73: name = property(get_name, set_name)
print(don.name)
don.name = "Margarida"
print(don.name)