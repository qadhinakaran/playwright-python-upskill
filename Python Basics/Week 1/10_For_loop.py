obj = [2, 3, 5, 7, 9]

for i in obj:
    print(i)

print("-------------")

#Output should be multiple of 2
for i in obj:
    print(i*2)

print("-------------")

#Print sum of first 5 natural numbers
summation = 0
for j in range(1, 6):
    summation += j
    print(summation)

print("-------------")

#For every iteration i value should increment 2
for i in range(1, 10, 2):
    print(i)



