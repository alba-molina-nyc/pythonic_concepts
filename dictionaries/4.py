# find value inside a dict

# Linear Search -> #o(n)
# visit each and every element in dict and see if thats the element we are looking for

myDict = {'name': 'Edy', 'age':26, 'address': 'London'}

def searchDict(dict,value):
    for key in dict:
        if dict[key] == value: 
            return f'this is the KEY : {key} && VAL: {value}'
    return f'the value {value} does not exist in this {dict}'

print(searchDict(myDict, 26))