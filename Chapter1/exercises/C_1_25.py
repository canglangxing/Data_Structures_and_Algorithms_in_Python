import string


def fun(line):
    for i in string.punctuation:
        while i in line:
            line = line.replace(i, '')
    return line


print(fun("Let's try, Mike."))
