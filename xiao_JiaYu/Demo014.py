'''
* 内容：接下来就是面向对象的三大特征:封装 、 继承 、 多态
*    classmethod 修饰符:classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
* data ：2019.06.25
* @author：fangbu
'''
class A:
    def __init__(self,a = None):
        self.a = a
    def test(self):
        print("A>>test")
class B:
    def __init__(self,b=None):
        self.b=b
    def test(self):
        print("B>>test")
class C(B,A):
    def __init__(self,a):
        A.__init__(self,a)
    def t(self):
        A.test(self)
        super().test()
        print("C>>test")
c = C("aa")
c.test()
c.t()

# 三.多态
'''
*1.什么是多态？ 
*   当子类和父类都存在相同的方法时，我们说，子类的方法覆盖了父类的方法，在代码运行的时候，总是会调用子类的方法。这样，我们就获得了继承的另一个好处：多态。 
*2.多态的实例 
*   简单工厂模式就是典型的多态体现：

让用户输入要选择的汉堡，他不需要知道内部是如何制作的，只要得到一个选择的汉堡实例对象就可以
'''
#创建汉堡的父类，并根据父类创建几个子类
class Hamburger:
    def make(self):
        print("您没有正确选择制作的汉堡，请重新输入")
class FishHamburger(Hamburger):
    def make(self):
        print("您的鱼肉汉堡已经制作好了")
class BeafHamburger(Hamburger):
    def make(self):
        print("您的牛肉汉堡已经制作好了")
class ChickenHamburger(Hamburger):
    def make(self):
        print("您的鸡肉汉堡已经制作好了")

#工厂类，用来判断用户输入的值并创建相应的对象
class HamburgerFactory:
    @classmethod
    def getinput(cls,temp):
        if temp == "1":
            ch = FishHamburger()
        elif temp == "2":
            ch = BeafHamburger()
        elif temp == "3":
            ch = ChickenHamburger()
        else:
            ch = Hamburger()
        return ch
#主方法，通过用户输入的值调用工厂的类方法
while True:
    temp = input("请输入您要制作汉堡的序号，1.鱼肉汉堡，2.牛肉汉堡，3.鸡肉汉堡")
    if temp == "1" or temp == "2" or temp == "3":
        ch = HamburgerFactory.getinput(temp)
        ch.make()
        break
    else:
        ch = Hamburger()
        ch.make()
        continue