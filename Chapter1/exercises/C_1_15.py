def fun(data):
    a = len(data)
    b = len(set(data))
    if a == b:
        return True
    else:
        return False
