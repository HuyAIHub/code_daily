class Car:
    #constructor
    def __init__(self,name , tenxe , masac):
        #lớp car có 3 thuộc tính : name , màu sắc , tenxe
        self.name = name
        self.tenxe = tenxe
        self.masac = masac
    # phương thức
    def chayxe(self):
        print("{} đang chạy trên đường.".format(self.name))
    def dungxe(self,mucdich):
        print("{} đang dừng để {}".format(self.tenxe,mucdich))

#lớp toyota mở rộng từ lớp cha
class toyota(Car):

    def __init__(self, hangxe, tenxe, mausac, nguyenlieu):
        # Gọi tới constructor của lớp cha (Car)
        # để gán giá trị vào thuộc tính của lớp cha.
        super().__init__(hangxe, tenxe, mausac)

        self.nguyenlieu = nguyenlieu

    # kế thừa phương thức cũ
    def chayxe(self):
        print("{} đang chay trên đường".format(self.tenxe))
    #ghi đè(override) phương thức cùng tên của lớp cha
    def dungxe(self,mucdich):
        print("{} dùng xe để {}".format(self.tenxe,mucdich))
        print("{} chạy bằng {}".format(self.tenxe,self.nguyenlieu))

# bổ sung thêm thành phần mới
    def nomay(self):
        print("{} đang nổ máy ".format(self.tenxe))

toyota1 = toyota("toyota","123","hồng","m1")
toyota2 = toyota("toyota","222","xanh","m2")
toyota3 = toyota("toyota","333","đen","m3")

toyota1.dungxe("nạp điện")
toyota2.chayxe()
toyota3.nomay()
#ôi chỉ có tôi và em bên những cái giljolkjlk

