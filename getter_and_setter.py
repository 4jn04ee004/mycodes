## Getter & Setter

class GS:

    def __init__(self, msg, name):
        self.__msg = msg
        self.__name = name


    def get_val(self):
        return self.__name

    def set_val(self, name):
        self.__name = name


a = GS("Hello", "You")
print(a.get_val())

a.set_val("World!")
print(a.get_val())
