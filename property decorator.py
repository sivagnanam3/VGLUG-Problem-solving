# PROPERTY DECORATOR
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Program for propery decorator")
    @ property
    def printall(self):
        return self.name+" Age is "+str(self.age)
user=student("Ragupathi",19)
user.printall
print(user.printall)
print(user.age)
print(user.name)
user.age=20
print(user.printall)
