"""
IN 
used to check if something exists in dict or not
"""

myDict = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuatro'}

#in operator only checks key
print('one' in myDict)


# to check values just use values()
print('tres' in myDict.values())


for key in myDict:
    print(key)
    print(myDict[key], 'to return value') #o(n)



