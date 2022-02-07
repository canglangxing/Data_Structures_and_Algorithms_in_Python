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


class SquareRootProgression(Progression):

    def __init__(self, start=65536):
        super().__init__(start)

    def _advance(self):
        self._current = self._current ** 0.5


if __name__ == '__main__':
    SquareRootProgression().print_progression(10)
