#module containing generic functions, strictly for practicing the structure and distribution of Python packages
#I will literally call methods included with Python and create functions that take a parameter, instead of using the methods normally


#list append 'function'
def listAdd(list, element):
   # if not list or element:
       # return None
    
    return list.append(element)

#list pop 'function'
def listPop(list, index):
    #if not list or index:
     #   return None
    
    return list.pop(index)

#list count 'function'
def listCount(list, value):
    #if not list or value:
     #   return None
    
    return list.count(value)

#list index 'function'
def listIndex(list, index):
    #if not list or index:
     #   return None
    
    return list.index(index)
