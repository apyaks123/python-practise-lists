# example from book
from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
Duck(bill = 'wide orange', tail = 'long')
print(duck.bill)
print (duck.tail)

# 2nd example similar
parts = {'bill': 'wilde orange', 'tail': 'long'}
duck2 = Duck(**parts)
print('2nd example: ')
print(duck2)
#Duck(bill = 'wide orange', tail = 'long')


#replace example
print('3rd example: replace function')
duck3 = duck2._replace(tail='magnificient', bill = 'crushing')
print(duck3)


