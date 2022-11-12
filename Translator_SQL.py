def requests_sql():

    post = input("Напишите название таблицы: ")

    aggregate_function = ''

    dict_aggregate_functions = {
        ('max', "максимальное", "наибольший") : 'max',
        ('min', "минимальное", "наименьший"): 'min',
        ('count', "количество"): 'count',
        ('avg', "среднее", "в среднеем"): 'avg'
    }


    choice_aggregate_function = input("Выбирите агригантные функцию: ").lower()

    for agg_funct in dict_aggregate_functions.keys():
        if choice_aggregate_function in agg_funct:
            aggregate_function = dict_aggregate_functions[agg_funct]

    choice_post = input("Выберите столбец: ")

    if choice_aggregate_function != 'z':
        result = f"SELECT {aggregate_function}({choice_post}) FROM {post}"
    else:
        result = f"SELECT {choice_post} FROM {post}"

    return result








# massive1 = ["Сколько", "Максимальное", "Минимальное", "Количество", "Все", ] # SELECT
# if s in  any({[сколько, количество]: 'count'}.keys()): request += count
# if s in  ({"Максимальное" : 'max'}.keys())
