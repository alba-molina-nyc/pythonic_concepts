# delete and slice


myList =['a', 'b', 'c', 'd', 'e', 'f']
print(myList[0:2])
print(myList[:1])
print(myList[1:])
print(myList[:])

myList[0:2] = ['x', 'y']

print(myList)

myList.pop(0) #o(n) delete from beginning because everything needs to shift
print(f'when you DO provide an index to the pop method{myList}')

myList.pop() # o(1) delete last element
print(f'when you do NOT  provide an index to pop method{myList}')


dList = ['a', 'c', 'p', 'q', 'r', 's']
print(f'{dList}, list without removing')
del dList[5]  #o(n) bc shift
print(f'{dList} providing index to the delete method')


del dList[0:2] # delete using slice and del method
print(f'{dList} using the SLICE Method and del method')


rList = ['j', 'k', 'l', 'm', 'n', 'f']
# use remove when you know the item you want to delete but maybe you do not know the index
rList.remove('j') #o(n) bc everything needs to shift 

print(f'{rList} after using REMOVE j method') 