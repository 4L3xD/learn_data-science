def eat(food, its_healthy):
    if its_healthy:
        final = ' porque é uma delícia!'
    else:
        final = '. Muito sódio!'
    return f'Estou comendo {food}{final}'

def sleep(hours):
    if hours > 8:
        return f'Putz! Dormi muito... zZ'
    else:
        return 'O processo de memorização depende de pelo menos 8 horas de sono para ser eficiente.'