#numbers = [x for x in range(1,40)]
numbers = 'The first three items in the list are:'
print(f'有{len(numbers)}个元素')
print(numbers)
q = numbers[0:16]    # 前 16 个元素
b = numbers[16:28]   # 第 17 到 28 个元素
z = numbers[28:39]   # 剩余 11 个元素
print("第一段：", q)
print("第二段：", b)
print("第三段：", z)
# 如果还想单独取前三个元素
first_three = numbers[:3]
print("前三个元素：", first_three)