def fun(line):
    vowel = ['a', 'e', 'i', 'o', 'u']
    num = 0
    for i in line:
        if i in vowel:
            num += 1
    return num
