def times(n):
    counts = 0
    while n >= 2:
        n = n//2
        counts += 1
    return counts
