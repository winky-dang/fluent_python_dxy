# # 把一个字符串变成Unicode码位的列表
# symbols = '$&^*^@*'
# codes = []
# for symbol in symbols:
#     codes.append(ord(symbol))
# print(codes)  # [36, 38, 94, 42, 94, 64, 42]


# 另一种写法。把一个字符串变成Unicode码位的列表
symbols = '$&^*^@*'
codes = [ord(symbol) for symbol in symbols]
print(codes)  # [36, 38, 94, 42, 94, 64, 42]

