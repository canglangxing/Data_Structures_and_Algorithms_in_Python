def min_max(data):
    if data:
        m = n = data[0]
        for i in data:
            if i > m:
                m = i
            if i < n:
                n = i
        return m, n
