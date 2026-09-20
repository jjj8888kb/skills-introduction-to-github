favorite_languages = { 
      'jen': ['python', 'rust'], #3个容器：字典，字符串，列表
      'sarah': ['c'], 
      'edward': ['rust', 'go'], 
      'phil': ['python', 'haskell'], 
      } 
#使用2个变量访问字典，分别是键和键值
for name,languages in favorite_languages.items():
      #判断 键值中的列表元素是否为1个
      if len(languages) == 1:
          print(f"{name.title()}'s favorite language is {languages[0].title()}.")
      else:  
            print(f"{name.title()}'s favorite languages are:") 
            for language in languages: 
                  print(f"\t{language.title()}")

