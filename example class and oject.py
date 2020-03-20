class car:
    # thuộc tính lớp
    loaixe = "ô tô"

    # thuộc tính đối tượng
    def __init__(self, tenxe, mausac, chatlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.chatlieu = chatlieu


# khởi tạo lớp car
lamborghini=car("aventador", "đen", "carbon")
mercedes = car("E250", "vang", "thép")
porche = car("911", "tím", "carbon")

# truy cập vào thuộc tính của lớp

print("porche là xe {}.".format(porche.__class__.loaixe))
print("mercedes là xe {}.".format(mercedes.__class__.loaixe))
print("lamborghini cũng là xe {}.".format(lamborghini.__class__.loaixe))

# access the instance attributes

print("xe {} có màu {}. làm bằng {}.".format(porche.tenxe, porche.mausac, porche.chatlieu))
print("xe {} có màu {}. làm bằng {}".format(mercedes.tenxe, mercedes.mausac, mercedes.chatlieu))
print("xe {} có màu {}. làm bằng {}".format(lamborghini.tenxe, lamborghini.mausac, lamborghini.chatlieu))
