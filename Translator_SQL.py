def requests_sql(name_of_table='', funct='' , name_of_colomn='', flag_uniq=False, flag_where=False, post_where='', post_condition='', flag_order_by=False, post_order_by='', asc_desc=True, flag_limit=False, post_limit=''):

    post = name_of_table
    aggregate_function = ''

    dict_aggregate_functions = {
        ('max', "максимальное", "наибольший") : 'max',
        ('min', "минимальное", "наименьший"): 'min',
        ('count', "количество"): 'count',
        ('avg', "среднее", "в среднеем"): 'avg'
    }


    choice_aggregate_function =  funct.lower()

    for agg_funct in dict_aggregate_functions.keys():
        if choice_aggregate_function in agg_funct:
            aggregate_function = dict_aggregate_functions[agg_funct]

    choice_post = name_of_colomn

    if choice_aggregate_function != '':
        result = f"SELECT {aggregate_function}({choice_post}) FROM {post}"
    else:
        result = f"SELECT {choice_post} FROM {post}"

    if flag_uniq:
        result += f" DISTINCT"

    if flag_where:
        where = post_where + post_condition
        result += f" WHERE {where}"

    if flag_order_by:
        order = post_order_by
        result += f" ORDER BY {order}"
        if asc_desc:
            result += ' DESC'

    if flag_limit:
        limit = post_limit
        result += f" LIMIT {limit}"


    return result