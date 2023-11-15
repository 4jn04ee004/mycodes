## Iterating collection

# Sets are unordered collections


s = {'x', 'y', 'b', 'c', 'a'}

for item in s:
    print(item)


## Infinite Sequence
    
class Squares:

    def __init__(self):
        self.i = 0

    def next_(self):
        result = self.i ** 2
        self.i = self.i + 1
        print(result)


sq = Squares()
sq.next_()
sq.next_()
sq.next_()
sq.next_()


# How to restart a sequence ? by creating a new instance

sq1 = sq = Squares()
sq1.next_()
sq1.next_()
sq1.next_()
sq1.next_()

print('*' * 50)

class Squares:

    def __init__(self, length):
        self.length = length
        self.i = 0

    def __len__(self):
        return self.length

    def next_(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result


sq = Squares(10)
print("Length of the sequence : ",len(sq))

while True:
    try:
        print(sq.next_())
    except StopIteration:
        break



## Uses of __next__
print('*' * 50)

class Squares:

    def __init__(self, length):
        self.length = length
        self.i = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Squares(3)

while True:
    try:
        print(next(sq))
    except StopIteration:
        break


print('*' * 50)

import random

class RandomNumber:

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

numbers = RandomNumber(3)


while True:
    try:
        print(next(numbers))
    except StopIteration:
        break

    
        

        
