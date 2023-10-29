processed = 0
good = 0
badValues = 0
badItems = 0
elseList = 0

todolist = ["red:14.2",
    "yellow.band",
     "23",
     "purple:-3",
     "yellow:band"]

for item in todolist:
    try:
        l = item.split(':')
        value = int(l[1])
        good += 1
    except ValueError:
        badValues += 1
    except IndexError:
        badItems += 1
    except:
        processed -= 1
    else:
        elseList += 1
    finally:
        processed += 1



print(processed)
print(good)
print(badValues)
print(badItems)
print(elseList)



for n in range(2,10) :
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n)



def f():
    yield True

try:
    g = f()
    h = next(g)
    assert h is True
    print("True")
    h = next(g)
    assert h is None
    print("None")
except AssertionError:
    print("Assertion failed")
except GeneratorExit:
    print("Exit")
except StopIteration:
    print("Stop")



title = 'Python Programming'
result = 65

res_show = f'The course is titled {title} and my result is {result}'
print(res_show)

print(F'The course is titled {title} and my result is {result}')

title = 'C++ Programming'
result = 85

print(res_show)





from string import *
method="METHODS"
def x(methods):
    method = str.swapcase(methods)
    print(("%(method)s" % locals()))
methods=str.swapcase(method[:-1])
x(methods)






i = 150
j = 300

if ((True == False) and (False in (False,))) == True:
    print(i)
elif (True == False) in (False,) == False:
    print(j)
else :
    print("No arithmetical operator proceeded")




class Services(object):
   def __init__(self):
      self.__testscore = 95

   def getScore(self):
      print(self.__testscore)

   def setScore(self, testscore):
      self.__testscore = testscore

servicesscore = Services()
servicesscore.getScore()
servicesscore.setScore(100)
servicesscore.getScore()
#print(servicesscore.__getScore)



def greet(greeting=None):
    if greeting:
        print(greeting)
    while True:
        greeting = (yield)
        print(greeting)




before = [1,2,3,4,5]

def bar(lst) :
    return lst.append(7)

after = bar(before)

print(after)
print(before)





employee = {
    "Beth": {
        "tel": "9876",
        "department": "IT",
        "responsibilities": [ "python", "perl", "bash" ]
        }
    }

# The company's data structure is updated by performing the actions below:

employee["Charles"] = employee["Beth"].copy()
employee["Charles"]["tel"] = "9912"
employee["Beth"]["tel"] = "9910"
employee["Beth"]["responsibilities"].remove("perl")

# Which of the following will result from executing the print statement below?

print(employee["Charles"]["tel"],employee["Charles"]["responsibilities"],employee["Beth"]["tel"],employee["Beth"]["responsibilities"])




data = [1,2,3,4,5,6]

def f1(x):
    return 3 * x

def f2(x):
    try:
        return x > 3
    except:
        return 0


result = list(map(f1, list(filter(f2, data))))
print(result)

x = 1
y = 2
z = 3

def bar(xx) :
    global y
    x = 4
    xx = 5
    y = 6
    z = 7

bar(x)


print(x,y,z)


