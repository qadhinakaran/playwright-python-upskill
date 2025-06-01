#To make sure what cases the condition make false
it = 4
while it >1:
    print(it)
    it = it-1
print("-------------")

#In output 3 shouldn't present
it1 = 4
while it1 >1:
    if it1 != 3:
        print(it1)
    it1 = it1-1
print("-------------")

#To use Break - It is used to hold/halt the loop abruptly
it = 4
while it >1:
    if it == 3:
        break
    print(it)
    it = it-1
    print("While loop is executed")
print("-------------")

#To use Continue - It is used to Skip current iteration
it = 10
while it > 1:
    if it == 9:
        it = it-1
        continue
    print(it)
    it = it-1