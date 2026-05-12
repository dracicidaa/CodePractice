#module containing generic functions, strictly for practicing the structure and distribution of Python packages
#I will literally call methods included with Python and create functions that take a parameter, instead of using the methods normally

#string split 'function'
def stringSplit(string, separator):
    #if not string or separator:
        #return None
    
    return string.split(separator)

#string join 'function'
def stringJoin(string, list):
    #if not string or list:
        #return None
    
    return string.join(list)

#string find 'function'
def stringFind(string, substring):
    #if not string or substring:
       # return None
    
    return string.find(substring)

#string statswith 'function'
def stringStart(string, prefix):
   # if not string or prefix:
       # return None
    
    return string.startswith(prefix)