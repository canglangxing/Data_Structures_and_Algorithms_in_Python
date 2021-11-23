num = input("Please enter three integers(separated by blank): ")
a, b, c = num.split()
a = int(a)
b = int(b)
c = int(c)

if a + b == c:
    print(f"{a}+{b}={c}")
elif a - b == c:
    print(f"{a}-{b}={c}")
elif a * b == c:
    print(f"{a}*{b}={c}")
elif a / b == c:
    print(f"{a}/{b}={c}")
elif a == b + c:
    print(f"{a}={b}+{c}")
elif a == b - c:
    print(f"{a}={b}-{c}")
elif a == b * c:
    print(f"{a}={b}*{c}")
elif a == b / c:
    print(f"{a}={b}/{c}")
else:
    print("No equation")
