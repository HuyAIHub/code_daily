class First:
    def getFirst(self):
        print("class First")
class Second:
    def getSecond(self):
        print("class Second")
class Third(First,Second):
    def getThird(self):
        print("class Third")
Third().getFirst()
Third().getSecond()
Third().getThird()
