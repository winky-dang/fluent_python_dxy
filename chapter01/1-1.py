import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]  # 因为__getitem__方法把[]操作交给了self._cards列表，所以deck类支持自动切片操作


beer_card = Card('7', 'diamonds')
print(beer_card)  # Card(rank='7', suit='diamonds')

deck = FrenchDeck()
print(len(deck))  # 52
# print(deck[0])  # Card(rank='2', suit='Spades')

# from random import choice
# print(choice(deck))  # Card(rank='K', suit='Spades')
# print(choice(deck))  # Card(rank='3', suit='hearts')
# print(choice(deck))  # Card(rank='8', suit='Spades')

# # 因为__getitem__方法把[]操作交给了self._cards列表，所以deck类支持自动切片操作
# print(deck[:3])  # [Card(rank='2', suit='Spades'), Card(rank='3', suit='Spades'), Card(rank='4', suit='Spades')]
# print(deck[12::13])  # [Card(rank='A', suit='Spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

# # 实现了__getitem__方法后，这一摞牌就变成可迭代的了
# for card in deck:
#     print(card)

# # 反向迭代也没关系
# for card in reversed(deck):
#     print(card)

# # 迭代通常是隐式的，譬如说一个集合类型没有实现__contians__方法，那么in运算符就会按顺序做一次迭代搜索。  因为FrenchDeck类是可迭代的，所以可以用in运算符
# print(Card('Q', 'hearts') in deck)  # True
# print(Card('7', 'beasts') in deck)  # False

# 排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# 有了 spades_high 函数，就能对这摞牌进行升序排序了
for card in sorted(deck, key=spades_high):
    print(card)

