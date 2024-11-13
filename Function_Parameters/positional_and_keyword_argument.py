def func(a, b, c):
    print(a, b, c)

func(10, 20, 30)


# Function with default values

def func(a, b=10, c=20):
    print(a, b, c)

func(100)
func(a=1000)


func(b=1000, c=10.5, a=2000)

# Function with formatting values

def func(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))

func(11, 12, 13)


