symbols = '$&^*^@*'
t = tuple(ord(symbol) for symbol in symbols)
print(t)  # (36, 38, 94, 42, 94, 64, 42)

import array
a = array.array('I', (ord(symbol) for symbol in symbols))
print(a)  # array('I', [36, 38, 94, 42, 94, 64, 42])
