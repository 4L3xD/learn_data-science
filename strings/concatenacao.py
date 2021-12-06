a = ['abc', 'def', 'ghi']

print(a)
for i in range(len(a)):
    for valor in a:
        if 'Pedro' not in valor:
            a[i] = valor + 'Pedro'
print(a)

a = ['abc', 'def', 'ghi']

r = input("Digite: ")
print(a)
for i in range(len(a)):
    for valor in a:
        if r not in valor:
            a[i] = valor + r
print(a)