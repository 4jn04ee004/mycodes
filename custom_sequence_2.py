# Custom sequence part 2

class MyClass:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Myclass(name = {self.name}"

    def __add__(self, other):
        return MyClass(self.name + other.name)

    def __iadd__(self, other):
        if isinstance(other, MyClass):
            self.name += other.name
        else:
            self.name += other

        return self

    

c1 = MyClass('Eric')
c2 = MyClass('Idle')

print(id(c1))
print(id(c2))

result = c1 + c2
print(id(result), result)


 
