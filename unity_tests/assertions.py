def soma_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos para que o resultado da soma seja positiva!'
    return a + b

retorno = soma_positivos(-2, 5)
print(retorno)

def comida_saudavel(comida):
    assert comida in [
        'frutas',
        'legumes',
        'verduras',
        'graos',
    ], 'A comida precisa ser saudável!'
    return f'Vida longa e próspera com {comida}!'

refeicao = input("Digite o tipo do alimento: ")
print(comida_saudavel(refeicao)) 

# shell: python -O assertions.py --> invalida os assertions na execução