class student:
    def __init__(self, maths, physics, chemistry):
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

    @staticmethod
    def hello():
            print("hello")

    def average_marks(self):
        avg = (self.maths+self.physics+self.chemistry)/3
        print("average of student : ",avg)

s1 = student(30, 50, 60)
s1.average_marks() 
s1.hello()       