# Searching a list

myList = [10,20,30,40,50,60,70,80,90]

#1 IN Operator -> o(n) complexity bc checks one by one

if 20 in myList:
    print(f'The item 20 exists at index: {myList.index(20)}')
else:
    print(f'the index does not exist in the list{myList}')


if 320 in myList:
    print(f'The item 20 exists at index: {myList.index(20)}')
else:
    print(f'the number 320 does not exist in the list{myList}')

# Linear Search (visit each element and checking if it is that element or not)

# Linear is (o)n, time o(1)


def linearSearch(list, value):
    for i in list:
        if i == value: 
            return f'{list.index(value)}'
    return f'the value {i} does not exist in the list {list}'

print(f'{linearSearch(myList, 50)}, linearSearch function')