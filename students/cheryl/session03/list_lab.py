#!/usr/bin/env python3
#
# Populate the list
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

# Add another fruit
new_fruit = input("pick another fruit:  ")
fruit.append(new_fruit)
print(fruit)

# Pick a number corresponding to a fruit
index = int(input("Pick a number: "))
if index > 0 and index <= len(fruit):
    print(fruit[index-1])
    
#Add another fruit to beginning of list
fruit = ["Plums"] + fruit
print(fruit)

#Add another to the beginning of the list
fruit.insert(0,"Pineapples")
print(fruit)

#Display all fruits beginning with a p
for each_fruit in fruit:
    if each_fruit[0] == 'P':
        print(each_fruit)

#Remove last from list
print(fruit)
fruit.pop()
print(fruit)

#Delete selected fruit
deleted_fruit = input("Enter a fruit to delete: ")
fruit.remove(deleted_fruit)
print(fruit)

#Delete all occurences 
fruit = fruit*2
print(fruit)
deleted_fruit = input("Enter a fruit to delete: ")
for i in range(fruit.count(deleted_fruit)):
        fruit.remove(deleted_fruit)
print(fruit)

#Keep the ones you like
for each in fruit:
    answer = ""
    while answer != "yes" or answer !="no":
        answer = input("Do you like {}? ".format(each))
        if answer == "no":
            fruit.remove(each)
            print(fruit)


