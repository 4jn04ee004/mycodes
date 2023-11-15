## Iterator

class Squares:

    def __init__(self, length):
        self.length = length
        self.i = 0

    def __next__(self):
        print('__next__ called')
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __iter__(self):
        print('__iter called')
        return self

sq = Squares(5)

for item in sq:
    print(item)



