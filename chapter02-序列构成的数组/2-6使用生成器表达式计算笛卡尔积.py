# 生成器表达式会在每次for循环运行时才生成一个组合，逐个产出元素。 t = tuple(ord(symbol) for symbol in symbols)
# 列表推导式会实现一次性构造一个完整列表。  codes = [ord(symbol) for symbol in symbols]
# 所以生成器可以避免额外的内存占用。

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s'%(c, s) for c in colors for s in sizes):
    print(tshirt)

# black S
# black M
# black L
# white S
# white M
# white L
