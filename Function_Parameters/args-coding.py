def func1(a, b, c):
    try:
        print(a)
        print(b)
        print(c)
    except Exception as e:
        print(e)

func1(10, 20, 30)

l1 = [1, 2, 3]

func1(*l1)

# If more numbers to be unpacked
l2 = [1,2,3,4]

func1(*l2)

def func2(a, b, *args):
    try:
        print(a)
        print(b)
        for i in args:
            print(i)
    except TypeError as e:
        print(e)

l3 = [11, 22, 33, 44, 55, 66]
func2(l3)

