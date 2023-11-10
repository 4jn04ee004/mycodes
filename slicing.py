## Slicing

s = slice(0,2)

print(type(s))
print(s.start)
print(s.stop)

data = []
for row in data:
    first_name = row[0:51]
    last_name = row[51:101]
    ssn = row[101:111]

    
range_first_name = slice(0,51)
range_last_name = slice(51, 101)
range_ssn = slice(101, 111)

for row in data:
    first_name = row[0:range_first_name]
    last_name = row[range_first_name:range_last_name]
    ssn = row[range_last_name:range_ssn]




l = 'python'
s1 = slice(1,5)

val = s1.indices(10)



start = -1
stop = 0

step = -1

length = len(l)

exp = list(range(*slice(start, stop, step).indices(length)))
print(exp)

text = ''

for i in exp:
    text.join(l[i])

print(text)


lst = list(l)
text = ''

for i in lst:
    text.join(i)
print(text)
