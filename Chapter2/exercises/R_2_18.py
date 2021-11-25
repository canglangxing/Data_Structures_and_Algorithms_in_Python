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


class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

    def __getitem__(self, item):
        answer = self._current
        current = self._current
        prev = self._prev
        for i in range(item):
            answer = next(self)
        self._prev, self._current = prev, current
        return answer


if __name__ == '__main__':
    f = FibonacciProgression(2, 2)
    print(f[8])
