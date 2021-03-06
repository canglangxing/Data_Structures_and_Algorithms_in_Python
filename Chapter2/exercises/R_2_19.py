class Progression:

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for _ in range(n)))


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

    def __getitem__(self, item):
        answer = self._current
        current = self._current
        for j in range(item):
            answer = next(self)
        self._current = current
        return answer


if __name__ == '__main__':
    a = ArithmeticProgression(128, 0)
    i = 0
    while a[i] < 2**20:
        i += 1
    else:
        print(i)
