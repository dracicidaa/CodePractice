#import stuff
from .module import dictGet, dictPop, setAdd, setComp, listAdd, listPop, listCount, listIndex, stringSplit, stringJoin, stringFind, stringStart

#time to go through all of the functions and see if I packaged everything correctly

#set things
lst = [7, 13, 59, 85, 44]
dicty = {'key0': 399,'key1': 426,'key2': 576}
stringy = 'cPGdXyrAiU'

#string work
print(stringStart(stringy, 'cPGd')) #true
print(stringFind(stringy, 'Xy'))    #4 ish
newStringy = stringSplit(stringy, 'd')  #['cPG', 'XryAiU']
print(newStringy)

#list work
print(listCount(lst, 13))   #1
lst = listAdd(lst, newStringy)
print(lst)
lst = listPop(lst, 3)   #85 should be missing
print(lst)

#string join
print(stringJoin('', lst))
