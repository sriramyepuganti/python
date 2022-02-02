# single line comment
""" Docstrings Python Comment """

# variables
# first character of the variable must be an alphabet or underscore ( _ )
# shoudl contain (A-Z,a-z,0-9)
# case senstive
# There are two types of variables in Python - Local and Global
# local var=> define inside function
# global var=> define outside the function 
# use 'global' keyword to define global var in function and use outside the function
# use 'del' keyword to delete the variable


# Assigning single value to multiple variables
assign1 = assign2 = assign3 = 50
print(assign1,assign2,assign3)

# Assigning multiple values to multiple variables:
mul1,mul2,mul3=10,20,30
print(mul1,mul2,mul3)

#object identity => same memory location
a1 = 50
b1 = a1
print("a1 location:",id(a1))
print("b1 location:",id(b1))
b1 = 100
print("b1 reassigned location:",id(b1))

# data types
# number => int, float, complex
# boolean
# sequence => str, tuple, list
# dictionary
# set

intVal = 1
floatVal = 1.0
complexVal = 1j
boolVal = True
strVal = "string"
tupleVal = (1,2,3,4)
listVal = [1,2,3,4]
setVal = { 1,2,3,4 }
dictVal = { "key1": "val1" }

print("integer:",intVal)
print("float:",floatVal)
print("complex:",complexVal)
print("bool:",boolVal)
print("string:",strVal)
print("tuple:",tupleVal)
print("list:",listVal)
print("set:",setVal)
print("dict:",dictVal)


# type checking
print("type checking",type(None))
print("is instance of class", isinstance(complexVal,complex))

# operators
op1 = 30
op2 = 20

#Arithmetic
print("Add",op1+op2)
print("Sub",op1-op2)
print("Mul",op1*op2)
print("Div",op1/op2)
print("Rem",op1%op2)
print("Pow",op1**op2)
print("FloorDiv",op1//op2)

# comparsion
print("30 is equal to 20:",op1 == op2)
print("30 is not equal to 20:",op1 != op2)
print("30 is less than or equal to 20:",op1 <= op2)
print("30 is greater than or equal to 20:",op1 >= op2)
print("30 is less than 20:",op1 < op2)
print("30 is greater than 20:",op1 > op2)

#assignment 
op1 = 20
op1+=1
print("Add:",op1)
op1-=1
print("Sub:",op1)
op1*=1
print("Mul:",op1)
op1**=2
print("Pow:",op1)
op1//=1
print("FloorDiv:",op1)
op1/=1
print("Div:",op1)
op1%=1
print("Rem:",op1)

#Bitwise
bit1 = 7
bit2 = 6
print("logical and:",bit1 & bit2)
print("logical or:",bit1 | bit2)
print("logical xor:",bit1 ^ bit2)
print("logical negation:",~ bit2)
print("logical left shift:",bit1 << 2)
print("logical right shift:",bit1 >> 2)

# Logical
print("And gate:",True and False)
print("Or gate:",True or True)
print("Not gate:",not True)

#Membership
print("in:",1 in [1,2,3])
print("not in:", 4 not in [1,2,3])

#Identity
obj1 = {}
obj2 = obj1
print("is:", obj1 is obj2)
print("is not:", obj1 is not obj2)

# print comment
def readComment():
    """ comment will be printed """
print(readComment.__doc__)

# if statement
ifVal = 30
if(ifVal==30):
    print("equal")
elif(ifVal>30):
    print("greater than")
else:
    print("else")

ternary = 3 if False else 5
print("ternary operator:", ternary)

# for loop
for i in range(0,5):
    print(i)
else: 
    print('loop completed')
whileVal = 5
while(whileVal > 0):
    print(whileVal)
    whileVal -= 1
else:
    print("loop completed")


#continue, break,pass
continueCount = 0  
continueStr = 'python'  
  
while continueCount < len(continueStr):   
    if continueStr[continueCount] == 'a' or continueStr[continueCount] == 't':   
        continueCount += 1  
        continue  
    elif(continueStr[continueCount]=='h'):
        break
    print('Current Letter :', continueStr[continueCount])   
    continueCount += 1  

class PassKeyword:
    pass
def passFun():
    pass
for i in range(1,5):
    pass

# Strings
# Updating the content of the strings is as easy as assigning it to a new string. The string object doesn't support item assignment i.e., A string can only be replaced with new string since its content cannot be partially replaced. Strings are immutable in Python.

str = "HELLO WORLD"
strDoc = """ Doc comment """
print(strDoc)
print(str*3)
print("Length of string:",len(str))
print("slice the string:",str[0:5])
print("slice the string with steps str(start,stop,step):",str[::2])
print("reverse the string:",str[::-1])
print("check val is present in string:",'Hell' in str)
# to print raw string
print(r'C://python37/test')
print("The string str : %s"%(str))
print("{} and {} both are the best friend".format("sriram","sai"))
print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))
print("capitalize",str.capitalize())
print("casefold",str.casefold())
print("center the string:",str.center(20))
print("count number of occurrence of sub string:",str.count("L"))
print("ends with:", str.endswith("LD"))
print("find:",str.find('L'))
print("join:", ",".join(['1','2','3']))

#Lists
# Python lists are mutable type its mean we can modify its element after it created.
# The lists are ordered and mutable type.
# l1*2 => l1 l1, l1 + l1 => l1 l1, ele in l1, len(l1), cmp(l1,l2), max(l1), min(l1), list(other_data_type)

list1 = [1,2,"Peter",4.50,"Ricky",5,6]  
list2 = [1,2,5,"Peter",4.50,"Ricky",6]  
print(list1==list2) # False

print('combine the list',list1 + list2)
newList = []
for i in range(0,10):
    newList.append(i) # add element
print(newList)
newList.remove(4) #remove element
print("remove:", newList)


# tuples
# Python Tuple is used to store the sequence of immutable Python objects.
# tuple is indexed in the same way as the lists.
# Unlike lists, the tuple items cannot be deleted by using the del keyword as tuples are immutable
# # t1*2 => t1 t1, t1 + t1 => t1 t1, ele in t1, len(t1), cmp(t1,t2), max(t1), min(t1), tuple(other_data_type)

tupleTest = ('str')
tupleTest1 = ('str',)
print(type(tupleTest))
print(type(tupleTest1))

# sets
# A Python set is the collection of the unordered items. Each element in the set must be unique, immutable, and the sets remove the duplicate elements.
# It can contain any type of element such as integer, float, tuple etc. But mutable elements (list, dictionary, set) can't be a member of set.
# clear,add,update, remove,discard,copy,pop,union,intersection, set(list)
setDays = {"Monday", "Tuesday", "Wednesday", "Thursday","Sunday"} 
setDays.add("Friday")
setDays.update(["Friday", "Saturday"]) # it accepts iterable ele
setDays.discard("Tuesday"); # it will not throw error if item not found
#setDays.remove("Tuesday"); # it will throw error if item not found
print(setDays)    
print(type(setDays))    
print("looping through the set elements ... ")    
for i in setDays:    
    print(i)

# dictionary 
# Python Dictionary is used to store the data in a key-value pair format. The dictionary is the data type in Python
# Keys must be a single element
# Value can be any type such as list, tuple, integer, etc.

# dict({}), del dic[0], pop(), i in dict.values(), x,y in dict.items(), len(), get(), copy(), has_key(), count(), 


# functions
# all the changes made to the reference inside the function revert back to the original value referred by the reference.
# Python provides the facility to pass the multiple keyword arguments which can be represented as **kwargs. It is similar as the *args but it stores the argument in the dictionary format.


def returnNone():
    return 
print(returnNone())

def returnSomething():
    return 50
    
print(returnSomething())

def change_list(list1):    
    list1.append(20)   
    list1.append(30)    
    print("list inside function = ",list1)    
    
#defining the list    
listForFun = [10,30,40,50]    
    
#calling the function     
change_list(listForFun)  
print("list outside function = ",listForFun)

def defaultArg(a,b=2):
    return a+b
print(defaultArg(10))

def varArgs(*var):
    print(var)
varArgs(1,2,3,45)

def KeywordArg(p,t):
    print(p,t)
KeywordArg(t=100,p=10)


lambdaExmp = lambda a:a**3
print(lambdaExmp(5))

# filter,map, reduce
from functools import reduce
filterExm = (1,2,3,4,5,6,7,8)
filterOutput = filter(lambda x: x%2,filterExm )
print(set(filterOutput))

mapOutput = map(lambda x: x*2, filterExm)
print(set(mapOutput))


reduceOutput = reduce(lambda a,b:a+b,filterExm)
print((reduceOutput))

