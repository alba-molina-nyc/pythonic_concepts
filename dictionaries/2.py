"""
UPDATE INSERT
How dictionaries are represented in memory
A hash table is a way of doing key-value look ups. You store the values in an array and tehn use a hash function to find the index of the array cell that correspondes to yourkey value pair
"""

myDict = {'name': 'Edy', 'age':26}

# to access get the key

myDict['age'] = 48 #o(1)

print(myDict)

# addition, if it does not exist then add key/value pair like this: 

myDict['address'] = 'London'

print(f'{myDict}, added address')  #o(1)