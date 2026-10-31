class student:
    def __init__(self, name , enroll, branch):
        self.name= name
        self.enroll = enroll
        self.branch= branch
    def intro(self):
        print("name of student:",self.name)
        print("enroll of student:",self.enroll)        
        print("branch of student:",self.branch)
        

stu = student("Atul", 123, "AIML")
stu.intro()