## Mutating an object
log = print
l = [1,2,3,4, 5]


log(id(l))

l[0] = 11
log(id(l))

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
alias = suits

def something(l):
    suits.append(None)

something(suits)

print(suits)
print(alias)


# Copying using slicing

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
alias = suits[:]

def something(l):
    suits.append(None)

something(suits)

print(suits)
print(alias)


from dis import dis

dis(compile('(1,2,3,"a")', 'string', 'eval'))
