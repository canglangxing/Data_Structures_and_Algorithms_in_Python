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


class AbsoluteDiffProgression(Progression):

    def __init__(self, first=2, second=200):
        super().__init__(first)
        self._prev = first + second

    def _advance(self):
        self._prev, self._current = self._current, abs(self._prev - self._current)


if __name__ == '__main__':
    AbsoluteDiffProgression().print_progression(10)
