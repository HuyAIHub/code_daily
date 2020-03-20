class Rectangle:
    'đây là rectangle class'
    # một phương thức dùng để tạo đối tượng (constrictor)
    def __int__(self,width,height):
        self.width = width
        self.height = height

    def getwidth(self):
        return self.width

    def getheight(self):
        return self.height

    #phương thức tính diện tích
    def getarea(self):
        return print(self.width*self.height)


width = int(input("nhập width:"))
height = int(input("nhập height:"))
p1 = Rectangle(width,height)
p1.getarea()
