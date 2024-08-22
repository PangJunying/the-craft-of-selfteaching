"""
 类(class)也有创作者和使用者。可以这样分步理解：
 1. 你创造了一个类，这时，你是创作者，从你的角度看，它就是一个类
 2. 你根据这个类的定义创建了很多个实例。
 2. 有人使用了你创造的类,这时,你是使用者,从使用者的角度看,它就是一个Object
 3. 类是一个模板,Object是一个实例
"""

import datetime

class Golem:
    population = 0 
    __life_span = 10
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.population += 1 # 类变量，所有实例共享
        
    def say_hi(self):
        print("Hi!")
        
    def cease(self):
        self.__active = False
        Golem.population -= 1
        # population -= 1
        
    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease()
        return self.__active    

class Running_golem(Golem):
    
    def run(self):
        print("Can't you see? I'm running...")
        
    def say_hi(self):
        print("Hey! Nice day, Huh?") # 重写父类的方法
        
                
g = Golem("Clay")
rg = Running_golem("Clay")

print(hasattr(Golem, 'population'))
print(hasattr(g, 'population'))
print(hasattr(Golem, '__life_span'))
print(hasattr(g, '__life_span'))
print(hasattr(g, '__active'))
Golem.population
print(setattr(Golem, 'population', 10))
Golem.population
x = Golem()
Golem.population
x.cease()
Golem.population
print(getattr(g, 'population'))
g.is_active()



# print(dir(rg))
# print(rg.__dict__)
# print(hasattr(rg,'built_year'))
# print(rg.run)
# print(rg.run())
# print(rg.name)
# print(rg.built_year)
# print("===")
# print(rg.say_hi()) # 实例方法，实例方法必须至少有一个参数，第一个参数通常被命名为self，它代表实例本身。
# print(help(rg))



# print(type(g))
# print(g.name) # g是一个根据Golem这个class创建的实例，所以g.name是一个实例变量，实例变量是每个实例特有的，每个实例的实例变量可以不同. 对于使用者来说，它就是一个Object。但是对于类来说实例变量是类的属性。
# print(type(g.name))
# print(g.built_year)
# print(type(g.built_year))
# print(g.say_hi)
# print(type(g.say_hi))
# print(g.say_hi())
# print(type(g.say_hi))
