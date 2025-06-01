#Declare Function
def greetMe(): # def->Identifier, GreetMe->Function name
    print("Good Morning")
greetMe()

#Parameterized Function
def greetMe(nam):
    print("Good Morning " + nam)
greetMe("Dhinakaran")

#Adding 2 integers
def addition(a , b):
    print(a + b)
addition(1, 2)

#Using return
def add(a, b):
    return a + b
print(add(10, 8))