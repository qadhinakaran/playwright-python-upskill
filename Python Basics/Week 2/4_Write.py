# Read the file and store all the lines in list
# Reverse the list
# Write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines() #[apple, ball, cat, dog, elephant]
    reversed(content) #[elephant, dog, cat, ball, apple]
    with open('reverse.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)