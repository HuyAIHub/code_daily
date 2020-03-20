#mình sẽ gọi phương thức getName và thuộc tính name của class Foo khi đang đứng ở class Bar
class Foo:
    name = "Foo"
    def getName(self):
        print("class: Foo")
class Bar(Foo):
    name = "Bar"
    def getName(self):
        print("Atribute name = " + super().name)
        super(Bar, self).getName()
Bar().getName()