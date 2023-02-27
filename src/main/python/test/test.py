import math

num = 3
if num % 2:
    print("奇数", end=" ")
else:
    print("偶数", end=" ")

result = None
if result:
    pass
else:
    print("什么收获都没有")
password = "123"
input_str = "abc123456"
print(input_str.find(password))

t = ("a", 'a', 12, "该校", '师生')
for i in t:
    print(i)
t1 = ('a',)
print(t1)

lst = [1, 2, 3]
lst.append(4)
print(lst)

# lst1 = [1, 2, 3]
# lst2 = lst1
# lst1.append(4)
#
# print(lst1)
# print(lst2)

lst1 = [1, 2, 3]
lst2 = lst1.copy()
lst1.append(4)
print(lst1)
# [1, 2, 3, 4]
print(lst2)
# [1, 2, 3]


sales = (("Peter", (78, 70, 65)),
         ("John", (88, 80, 85)),
         ("Tony", (90, 99, 95)),
         ("Henry", (80, 70, 55)),
         ("Mike", (95, 90, 95)),)

print(sales[1][0])
# 现在我们将计算出每人的总销售额，
# 并按销售额从多到少，
# 存放到一个列表里

top_sales = []
for name, quarter_amount in sales:
    total_amount = sum(quarter_amount)
    top_sales.append((name, total_amount))
top_sales.sort(key=lambda x: x[1], reverse=False)
print(top_sales)

# sales = {'Peter': 213, 'John': 253, 'Tony': 284, 'Henry': 205, 'Mike': 280}
sales_dict = dict(top_sales)
print(sales_dict.get("Peter"))

for key_value in sales_dict.items():
    print(key_value)

for key, value in sales_dict.items():
    print(key, value)

sales_dict.get("zyz", 0)

print()

for key, value in sales_dict.items():
    print(key, value)

nums = {1, 2, 3, 4, 5}


def hello(name_input):
    print(name_input)


hello(1)


def hello(name='Anonym', sex='女'):
    if sex == '男':
        print("Hello, Mr", name)
    elif sex == '女':
        print("Hello, Miss", name)


hello()


#
# class Dog:
#     pass


class Dog:
    def __init__(self, size):
        self.breed = "日本狗"
        self.color = "黑"
        self.size = size

    def __init__(self, size, color, breed='土狗'):
        self.breed = breed
        self.color = color
        self.size = size

    # def __init__(self):
    #     self.breed = None
    #     self.color = None
    #     self.size = None

    def eat(self):
        print("I like bones")

    def run(self):
        print("I'll catch you.")

    def bark(self):
        print('我是一只%s型%s色的%s' % (self.size, self.color, self.breed))


# dog = Dog()
# print(type(dog))
#
# print(dog.bark())

# dog_aa = Dog(12, "黑", "阿拉斯加")
# print(dog_aa.bark())
#
# type(1)
# type('abc')
# type([])

# dog_bb = Dog("大")
# print(dog_bb.bark())


print(math.sqrt(4))
