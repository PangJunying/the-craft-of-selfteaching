"""
 类(class)也有创作者和使用者。可以这样分步理解：
 1. 你创造了一个类，这时，你是创作者，从你的角度看，它就是一个类
 2. 你根据这个类的定义创建了很多个实例。
 2. 有人使用了你创造的类,这时,你是使用者,从使用者的角度看,它就是一个Object
 3. 类是一个模板,Object是一个实例
"""

import datetime

class Golem:
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
    def say_hi(self):
        print("Hi!")

class Running_golem(Golem):
    
    def run(self):
        print("Can't you see? I'm running...")
                
g = Golem("Clay")
rg = Running_golem("Clay")

print(rg.run)
print(rg.run())
print(rg.name)
print(rg.built_year)
print(rg.say_hi()) # 实例方法，实例方法必须至少有一个参数，第一个参数通常被命名为self，它代表实例本身。

# print(type(g))
# print(g.name) # g是一个根据Golem这个class创建的实例，所以g.name是一个实例变量，实例变量是每个实例特有的，每个实例的实例变量可以不同. 对于使用者来说，它就是一个Object。但是对于类来说实例变量是类的属性。
# print(type(g.name))
# print(g.built_year)
# print(type(g.built_year))
# print(g.say_hi)
# print(type(g.say_hi))
# print(g.say_hi())
# print(type(g.say_hi))
