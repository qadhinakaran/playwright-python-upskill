file = open('test.txt')
# Read all the content in the file
# print(file.read())

# Read n number of character by passing parameter
# print(file.read(8))

# Read content line by line -> file.readline()
print(file.readline())
print(file.readline())


file.close()