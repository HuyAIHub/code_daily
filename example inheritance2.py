class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        print("name: %s"%(self.name))
    def getAge(self):
        print("age: %d"%(self.age))
    def getsex(self):
        print("sex: %s"%(self.sex))
class Male(person):
    sex = "Male"
male = Male("nguyễn thị hồng nhung",18)
male.getAge()
male.getName()
male.getsex()