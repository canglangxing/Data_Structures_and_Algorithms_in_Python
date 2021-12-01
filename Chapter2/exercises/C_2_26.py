class ReversedSequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(self._seq)

    def __next__(self):
        self._k -= 1
        if self._k >= 0:
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self


if __name__ == '__main__':
    s = ReversedSequenceIterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
