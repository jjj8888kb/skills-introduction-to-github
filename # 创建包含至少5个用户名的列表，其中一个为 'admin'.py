# 创建包含至少5个用户名的列表，其中一个为 'admin'
usernames = ['admin', 'Jaden', 'Eric', 'Alice', 'Bob']

# 遍历用户名列表，打印问候消息
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")