spam = ['apples', 'bananas', 'tofu', 'cats']

def CommaCode(list):
    tempList = list
    tempList[-1] = 'and ' + tempList[-1]
    str = ''
    for i in range(0, len(tempList)-1):
        str += tempList[i] + ', '  
    str += tempList[-1] + '.' 
    return str
print(CommaCode(spam))