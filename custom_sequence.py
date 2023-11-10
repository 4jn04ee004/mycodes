## Custom Sequence

my_list = [1,2,3,4,5]

print(len(my_list))
print(my_list.__len__())
print(my_list.__getitem__(2))

print(my_list.__getitem__(slice(None, None, -1)))

index = 0

while True:
    try:
        item = my_list.__getitem__(index)
    except IndexError:
        break

    print(item ** 2)
    index += 1



class Silly:

    def __init__(self, n):
        self.n = n

    def __len__(self):
        print("Called __len__")
        return self.n

    def __getitem__(self, value):
        if value < 0 or value > self.n:
            raise IndexError
        
        print(f"You Requested Item at {value}")
        return "This is a silly element"


silly = Silly(10)
len(silly)
        
# silly.__getitem__(100)
    
for item in silly:
    print(item)


from functools import lru_cache

@lru_cache(2*10)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))


class Fib:

    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0 or s > self.n:
                raise IndexError
            return Fib._fib(s)

    @staticmethod
    @lru_cache(2*10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    
        
            
f = Fib(8)

