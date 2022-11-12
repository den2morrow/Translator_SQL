from Interfece import *
def requests_sql(a,b,c):

    post = a

    aggregate_function = ''

    dict_aggregate_functions = {
        ('max', "максимальное", "наибольший") : 'max',
        ('min', "минимальное", "наименьший"): 'min',
        ('count', "количество"): 'count',
        ('avg', "среднее", "в среднеем"): 'avg'
    }


    choice_aggregate_function =  b.lower()

    for agg_funct in dict_aggregate_functions.keys():
        if choice_aggregate_function in agg_funct:
            aggregate_function = dict_aggregate_functions[agg_funct]

    choice_post = c

    if choice_aggregate_function != 'z':
        result = f"SELECT {aggregate_function}({choice_post}) FROM {post}"
    else:
        result = f"SELECT {choice_post} FROM {post}"

    return result








# massive1 = ["Сколько", "Максимальное", "Минимальное", "Количество", "Все", ] # SELECT
# if s in  any({[сколько, количество]: 'count'}.keys()): request += count
# if s in  ({"Максимальное" : 'max'}.keys())
