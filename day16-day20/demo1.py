"""
    生成式（推导式）的用法
    可以用来生成列表、字典和集合
"""
price = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造成一个新的字典
price2 = {key: value for key, value in price.items() if value > 100}
print(price2)
