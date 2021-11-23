def reverse_input():
    input_line = []
    while True:
        try:
            input_line.append(input())
        except EOFError:
            for i in reversed(input_line):
                print(i)
            break


reverse_input()
