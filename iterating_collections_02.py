## Iterating Over Sqaures

s = {'x', 'y', 'b', 'c', 'a'}

for item in s:
    print(item)

class Squares:

    def __init__(self, length):
        self.i = 0
        self.length = length

    def __len__(self):
        return self.length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Squares(10)

while True:
    try:
        print()
        print(len(sq))
        print(next(sq))
    except StopIteration:
        break





import random

class RandomNumbers:

    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max

        self.num_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self.range_min, self.range_max)
        
numbers = RandomNumbers(5)

while True:
    try:
        print(next(numbers))
    except StopIteration:
        break

