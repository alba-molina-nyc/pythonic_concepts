# traverse through dicitonary, visiting all pairs one by one

myDict = {'name': 'Edy', 'age':26, 'address': 'London'}


def traverseDict(dict):
    for key in dict:
        print(f'{key} -> {dict[key]}') 

traverseDict(myDict)