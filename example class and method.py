class car:
    # thuộc tính đối tượng
    def __init__(self,tenxe,mausac,chatlieu):
        self.tenxe = tenxe
        self.mausac= mausac
        self.chatlieu = chatlieu
    # phương thức
    def dungxe(self,mucdich):
        return "{} đang dừng xe để {}".format(self.tenxe,mucdich)
    def chayxe(self):
        return "{} đang chay xe".format(self.tenxe)
    def nomay(self):
        return "{} đang nổ máy".format(self.tenxe)
toyota = car("Toyota", "Đỏ", "Điện")
lamborghini = car("Lamborghini", "Vàng", "Deisel")
porsche = car("Porsche", "Xanh", "Gas")

print(toyota.dungxe("đổ xăng"))
print(lamborghini.chayxe())
print(porsche.nomay())
