# insert/update

# list[index] = item_assigning

myList = [1,2,3,4,5,6,7]
print(myList)

myList[0] = 10
print(myList)

myList[-1] = 20
print(myList)

myList[1] = 3.5
print(myList)


"""
FOUR WAYS TO INSERT TO LIST
1. beginning
2. any given place
3. end
4. inserting another list to the list
"""

# insert -> inserts any given location of a list

iList = [1,2,3,4]

# insert method -> list_name.insert(index, item_inserting)
iList.insert(0,11) #o(n)
print(iList)

# ADD TO END OF LIST append method -> list_name.append(item_appending) 
aList = [1,2,3,495]

aList.append(0) #o(1)
print(aList)


# ADD NEW LIST extend method
eList = [10,2,3]
print(eList)
e_List = [5,6,7]
eList.extend(e_List) #o(n)
print(f'{eList}, after extending')