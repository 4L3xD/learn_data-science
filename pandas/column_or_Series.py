import pandas as pd

column = pd.Series(
    [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9],
    name="Numbers"
)

#print(column.values) #out: [0 1 2 3 4 4 5 6 7 8 9]
#print(column.index) #out: RangeIndex(start=0, stop=11, step=1)
#column[0] = 'x' #substitui valor na posição do índice
#print(column)
#print(column.describe())

column = pd.Series(
    [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9],
    name="Numbers",
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
)

#print(column)
#print(column['a']) #imprime o valor correspondente ao índice
#print(column[['a']]) #imprime o índice e seu valo respectivo
#print(column[['a', 'b', 'c']]) #imprime os índices selecionados e seus respectivos valores 
#print(column[column % 2 == 0])
#print('b' in column)
#print('b' in column and print(column[['b']]))


from pandas import Series, DataFrame 
#                "population": [46.649132, 17.463349, 21.411923, 14985284]
population = {"SP": 46.6, "RJ": 17.4, "MG": 21.4, "BA": 14.9}
population_cities = Series(population)

states = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia"]
pop_city = []
for pop in population:
    pop_city.append(population[pop])
column_states = Series(pop_city, index=states)
#print(column_states)

column_states = Series([population["SP"], population["RJ"], population["MG"], population["BA"]], index=states)
#print(column_states)


population = {"SP": [46.6], "RJ": [17.4], "MG": [21.4], "BA": [14.9]}
cities_pop = Series([value for tag in population for value in population[tag]], index=[tag for tag in population])
#print(cities_pop)

#print(pd.isnull(column_states))
#print(population_cities + cities_pop)

population = {
                "cities": ["SP", "RJ", "MG", "BA"],
                "population": [46.6, 17.4, 21.4, 14.9]
            }
population_cities = DataFrame(population)
#print(population_cities)

frame = DataFrame(population, columns=["cities", "population"], index=["Maior população", "Segunda maior população", "Terceira maior população", "Quarta maior população"])
#print(frame)

frame['Column'] = frame.cities == "SP"
#print(frame)

frame = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
frame['g'] = 7
#print(frame[['a', 'b', 'c', 'd']])

frame.name = "numbers"
frame.index.name = "índices"
print(frame)

#p. 128
