#module containing generic functions, strictly for practicing the structure and distribution of Python packages
#I will literally call methods included with Python and create functions that take a parameter, instead of using the methods normally

#set add 'function'
def setAdd(set, item):
    if not set or item:
        return None
    
    return set.add(item)

#set difference 'function'
def setComp(set, otherSet):
    if not set or otherSet:
        return None
    
    return set.difference(otherSet)