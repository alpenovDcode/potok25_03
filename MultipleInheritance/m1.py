# class Animal:
#     def eat(self):
#         return "Eating"
#
# class Dog(Animal):
#     def eat(self):
#         return "Dog"
#
# class Bird(Animal):
#     def eat(self):
#         return "Bird"
#
# class Bird2(Animal):
#     def eat(self):
#         return "Bird2"
#
# class Monkey(Bird, Bird2, Dog):
#     pass
# '''
# Animal
#     - Dog
#     - Bird
#         - Monkey
# '''
# m1 = Monkey()
# print(m1.eat())
# print(Monkey.mro()) # Method Resolution Order (порядок разрешения методов)
#
# # [<class '__main__.Monkey'>,
# # <class '__main__.Dog'>, <class '__main__.Bird'>,
# # <class '__main__.Animal'>,
# # <class 'object'>]

# Diamond Problem(алмазный паттерн)

# class A:
#     def say_hello(self):
#         return "Hello from A"
#
# class B:
#     def say_hello(self):
#         return "Hello from B"
#
# class C(A, B):
#     def say_hello(self):
#         return B.say_hello(self)
#
# c = C()
# print(c.say_hello())


class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        return f"{self.name} is sleeping."


class Walkable:
    def walk(self):
        return f"{self.name} is walking."


class Swimmable:
    def swim(self):
        return f"{self.name} is swimming."

class Flyable:
    def fly(self):
        return f"{self.name} is flying."

class Dog(Animal, Walkable):
    def __init__(self, name):
        Animal.__init__(self, name)

class Duck(Animal, Walkable, Swimmable, Flyable):
    def __init__(self, name):
        Animal.__init__(self, name)


dog = Dog("Buddy")
print(dog.sleep())
print(dog.walk())
print(20*'-')
duck = Duck("DonaldDuck")
print(duck.walk())
print(duck.sleep())
print(duck.swim())
print(duck.fly())
print(20*'-')
print(Dog.mro())
print(Duck.mro())


'''
[<class '__main__.Dog'>, <class '__main__.Animal'>, 
<class '__main__.Walkable'>, <class 'object'>]

[<class '__main__.Duck'>, <class '__main__.Animal'>, 
<class '__main__.Walkable'>, <class '__main__.Swimmable'>, 
<class '__main__.Flyable'>, <class 'object'>]
'''

