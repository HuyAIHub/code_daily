class Foo:
    name = "haha"
    def getName(self):
        print("class: Foo")
class Bar(Foo):
    name = "baba"
    def getName(self):
        print("class: Bar")
a = Foo().name
print(a)
Foo().getName()
b = Bar().name
print(b)
Bar().getName()