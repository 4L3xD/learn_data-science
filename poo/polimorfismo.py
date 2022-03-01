class Animal():
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar este método!")

    def comer(self):
        print(f"{self.__nome}, está comendo!")


"""
class Burro(Animal):
    def __init__(self, nome):
        Animal.__init__(self, nome)
        #super().__init__(nome)
    
Burro("Donkey").falar() #NotImplementedError: A classe filha precisa implementar este método!
"""

class Burro(Animal):
    def __init__(self, nome):
        #Animal.__init__(self, nome)
        super().__init__(nome)
    
    def falar(self):
        print(f"{self._Animal__nome}, fala Hee-haw!")

Burro("Donkey").falar()