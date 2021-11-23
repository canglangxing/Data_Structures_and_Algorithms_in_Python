def arithmetic_performance(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return 'Invalid operator'


def convert_to_number(input_str):
    try:
        return float(input_str)
    except ValueError:
        print('Invalid input')
        return None


def simple_calculator():
    operators = ['+', '-', '*', '/']
    first_number = None
    operator_symbol = None
    second_number = None
    input_str = 'Start'
    while input_str != '' and input_str != 'Esc':
        input_str = input()
        if input_str == '' or input_str == 'Esc':
            break
        elif first_number is None:
            first_number = convert_to_number(input_str)
        elif operator_symbol is None:
            if input_str in operators:
                operator_symbol = input_str
            else:
                print('Invalid operator')
        elif second_number is None:
            second_number = convert_to_number(input_str)
        else:
            if input_str == '=':
                print(f'{first_number} {operator_symbol} {second_number} = '
                      f'{arithmetic_performance(first_number, operator_symbol, second_number)}')
                first_number = operator_symbol = second_number = None
            else:
                print('Invalid operator')


simple_calculator()
