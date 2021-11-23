from random import randrange
from random import choice


def typo(message, error_range):
    while True:
        error_spot = randrange(0, len(message))
        error_character = choice(error_range)
        message_list = list(message)
        if message_list[error_spot] == ' ' or message_list[error_spot] == error_character:
            continue
        else:
            message_list[error_spot] = error_character
            return ''.join(message_list)


def copy_typo(message, times, typo_times):
    error_range = [chr(i) for i in range(65, 90)] + [chr(j) for j in range(97, 122)]
    error_lines = set()
    while len(error_lines) < typo_times:
        error_line = randrange(0, times)
        error_lines.add(error_line)

    for i in range(times):
        if i not in error_lines:
            print(f'{message}   line {i + 1}')
        else:
            print(f'{typo(message, error_range)}   line {i + 1} <- wrong line')


copy_typo('I will never spam my friends again', 100, 8)
