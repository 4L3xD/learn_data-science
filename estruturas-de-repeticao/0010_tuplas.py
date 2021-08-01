# Referências: https://penseallen.github.io/PensePython2e/12-tuplas.html

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname, domain)

x = (2, 7)
print(divmod(*x))


def sumall(*args):
    z = 0
    for y in args:
        z += y
    print(z)

sumall(1, 2, 3, 4, 5)

