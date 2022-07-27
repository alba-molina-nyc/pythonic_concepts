# delete

myDict = {'name': 'Edy', 'age':26, 'address': 'London', 'education': 'master'}
print(f'{myDict} before')

myDict.pop('name')

print(f'{myDict} after popping off name')


myDict.popitem() # remove and return a pair at random

print(myDict)

aDict = {'name': 'Edy', 'age':26, 'address': 'London', 'education': 'master'}

aDict.clear() 
print(f'{aDict} deletes all items')


dDict =  {'name': 'Edy', 'age':26, 'address': 'London', 'education': 'master'}


del dDict['age'] #delete any, or entire dict #o(1)

print(dDict)