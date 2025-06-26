file = open('test.txt')

# To iterate and print all the values in the file
# Method - 1

# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()

# Method - 1 ---> Readlines concept
# Using read line, one list will be created. From that list we can iterate, retrieve and print all the values in the file
# value = [apple, ball, cat, dog, elephant]

for line in file.readlines():
    print(line)

