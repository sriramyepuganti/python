# list functions

listExm = [1,2,3,4,6,5,7,10,9,8]
lengthOfList = len(listExm)
listFirstValue = listExm[0]
listNegVal = listExm[-1]
listSomeVal = listExm[2:9]
checkValExist = 1 in listExm
# print(sum(listExm)) # print sum of all elements
listExm[0] = "set" # set value
listExm[1:3] = ["test1","test2"] # set multiple values
listExm.insert(0, "insert") # update values
listExm.append(11) # append value
listExm.extend([12,13]) # attach two list
listExm.remove("set") # remove particluar value
listExm.pop(0) # remove value from index
listExm.index(10) # return index of value 10

del listExm[0] # del the value
del listExm[0]
#listExm.clear() # clear the list
for val in listExm:
    # print(val)
    pass
for key in range(len(listExm)):
    # print(key)
    pass

newListExm = [ x for x in listExm ]
newListExm.sort() # sort list
newListExm.sort(reverse=True)
def listSort(values):
    return abs(values-5)
newListExm.sort(key=listSort) # assign function to sort
newListExm.reverse() # reverse list
#copyList = listExm.copy() # copy the list
del listExm # del list


# tuple functions

tupleExm = (0,1,2,3,4,5)

tupleLen = len(tupleExm)
tupleVal = tupleExm[0]
tupleNegIndex = tupleExm[-1]
tupleRange = tupleExm[1:4] 
tupleExists = 2 in tupleExm # check val exists or not
# loops example => follow list examples
tupleCount = tupleExm.count(1) # count the no. times value occured in tuple
tupleIndex = tupleExm.index(3) # return the position of that value


# set functions

setExm = { "test3","test4","test1","test2"}
setLength = len(setExm) # lenght of set
for x in setExm:
    # print(x)
    pass

setExm.add("test5") # add item to set
setExm.remove("test5") # remove item, If the item to remove does not exist, remove() will raise an error.
setExm.discard("test5") # If the item to remove does not exist, discard() will NOT raise an error.
setExm.update(("test6","test7")) # merge two sets into first one
setExm3 = setExm.union(("test1","test9")) # merge two and return new one
setExm.intersection_update(setExm3) # make set contains common ele
intersectionSet = setExm.intersection(setExm3) # return new set contains common ele
setExm.symmetric_difference_update(setExm3)  # method will keep only the elements that are NOT present in both sets.
differenceSet = setExm.symmetric_difference(setExm3) # method will return a new set, that contains only the elements that are NOT present in both sets.
setExm.pop() # Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
#setExm.clear() # clear the set

del setExm # del the set



# dictionary functions
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

dictLen = len(thisdict)
dictVal = thisdict['brand'] #get val
dictVal1 = thisdict.get('brand') #get val
dictKeys = thisdict.keys() # get keys
dictValues = thisdict.values() # get values
distToSet = thisdict.items() # method will return each item in a dictionary, as tuples in a list.
dictKeys = dict.fromkeys(thisdict)
print(dictKeys)
checkDictKey = "brand" in thisdict
thisdict["brand"] = "Tesla" # update or set
thisdict.update({"id":1}) # update or add
thisdict.pop("id") # pop() method removes the item with the specified key name:
# thisdict.pop() it will throw a error
thisdict.popitem() # method removes the last inserted item (in versions before 3.7, a random item is removed instead):
del thisdict["model"] # del
thisdict.clear() # method empties the dictionary:
# for loops follow list
# copy() to create a new dictionary
# setDefault: method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value, see example below