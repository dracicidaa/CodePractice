#module containing generic functions, strictly for practicing the structure and distribution of Python packages
#I will literally call methods included with Python and create functions that take a parameter, instead of using the methods normally

#dictionary get 'function'
def dictGet(dict, key):
    if not dict or key:
        return None
    
    return dict.get(key)

#dictionary pop 'function'
def dictPop(dict, key):
    if not dict or key:
        return None
    
    return dict.pop(key)
