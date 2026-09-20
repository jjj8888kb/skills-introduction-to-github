# 创建一个邀请名单（至少三人）
guests = ["李白", "爱因斯坦", "居里夫人"]
# 遍历名单，打印邀请消息
for guest in guests:
    print(f"{guest}，我诚挚地邀请您与我共进晚餐。")
print("居里夫人无法赴约")
guests[2] ="毛主席"
for guest in guests:
    print(f"{guest}，我诚挚地邀请您与我共进晚餐。")
print("我找到一张更大的桌子，可以接纳更多客人")
guests.insert(0,'库里')
guests.insert(2,'阿达')
guests.append('张三')
print(f'共有{len(guests)}位客人来共进晚餐')
for guest in guests:
    print(f"{guest}，我诚挚地邀请您与我共进晚餐。")
print("由于桌子买不到，只能邀请俩位")
popped = [guests.pop(0) for _ in range(4)]
popped_str = ",".join(popped)
guests_str = ",".join(guests)
print (f"{popped_str},抱歉我无法与您共进晚餐")
print(f"{guests_str}，我诚挚地邀请您与我共进晚餐。")
guests.clear()    # 删除所有元素
print("名单为空白")
