class Con:
    num = 100
    def __init__(self): #init -> is a keyword to declare constructor in Python
        print("I am called automatically")

    def getData(self):
        print("I am called using object")

obj = Con()
print(obj.num)
obj.getData()
