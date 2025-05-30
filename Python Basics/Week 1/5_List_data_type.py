value = [1, 2, "Sky", 4, 5]

print(value[0])
print(value[1])

# To know the value of the last index
print(value[-1])
print(value[1:4])

#To insert new variable in the list
value.insert(2, "Earth")
print(value)

#To insert new variable in the end
value.append("End")
print(value)

#To update the existing variable in the list
value[1]=18
print(value)

#To delete the existing value in the list
del value[4]
print(value)