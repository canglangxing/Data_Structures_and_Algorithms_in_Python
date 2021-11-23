def fun(data):
    for i in data:
        for j in data:
            if i * j % 2 == 1 and i != j:
                return True
            else:
                return False
