myUniqueList = []
def addMyUniqueList(a):
    if a not in myUniqueList:
        myUniqueList.append(a)
        return True
    else:
        return False
addMyUniqueList(1)
addMyUniqueList('a')
addMyUniqueList(['a', 'b'])
print(myUniqueList)