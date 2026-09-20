current_users = ['admin','asdsada','sadasdasd','asdasdad','asdada']
new_users = ['admin','asdsada','SAdasdasd','Fghfghg','vbnvbn']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:  #因为new_users是列表里面装了字符串，所以使用的变量为字符串。
    if new_user.lower() in current_users:
        print(f'{new_user}已被使用，请使用其他名称')
    else:
        print(f'{new_user}未被使用，是否使用')