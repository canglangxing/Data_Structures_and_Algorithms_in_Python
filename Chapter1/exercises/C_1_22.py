def fun(data_a, data_b):
    if len(data_a) != len(data_b):
        return False
    else:
        return [data_a[i] * data_b[i] for i in range(len(data_a))]
