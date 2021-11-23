from random import randrange


def birthday_paradox(people_number, trial_times):
    count = 0
    for i in range(trial_times):
        birthday = [randrange(0, 365) for i in range(people_number)]
        if len(set(birthday)) != len(birthday):
            count += 1
    print(f'For {people_number} people, the probability is approximately: {count/trial_times}')


birthday_paradox(23, 1000)
