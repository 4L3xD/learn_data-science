import unittest
from atividades_unittests import eat, sleep

class ActivitiesTests(unittest.TestCase):
    def test_eat_healthy(self):
        """Testando o retorno de comida saudável! :P"""
        self.assertEqual(
            eat('quiabo', True),
            'Estou comendo quiabo porque é uma delícia!'
        )

    def test_eat_tasty(self):
        """Testando o retorno de comida não saudável! :s"""
        self.assertEqual(
            eat(food='pizza', its_healthy=False),
            'Estou comendo pizza. Muito sódio!'
        )

    def test_sleep_a_lot(self):
        """Testando o retorno de dormir pouco! :'("""
        self.assertEqual(
            sleep(4),
            'O processo de memorização depende de pelo menos 8 horas de sono para ser eficiente.'
        )
    
    def test_sleep_a_bit(self):
        """Testando o retorno de dormir muito! :)"""
        self.assertEqual(
            sleep(10),
            'Putz! Dormi muito... zZ'
        )


if __name__ == '__main__':
    unittest.main()


#python testes_unittests.py -v
#-v == verbose: mostra mais detalhes dos testes

"""
test_eat_healthy (__main__.ActivitiesTests)
Testando o retorno de comida saudável! :P ... ok
test_eat_tasty (__main__.ActivitiesTests)
Testando o retorno de comida não saudável! :s ... ok
test_sleep_a_bit (__main__.ActivitiesTests)
Testando o retorno de dormir muito! :) ... ok
test_sleep_a_lot (__main__.ActivitiesTests)
Testando o retorno de dormir pouco! :'( ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
"""