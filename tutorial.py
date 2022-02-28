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
# print("casefold",str.casefold())
print("center the string:",str.center(20))
print("count number of occurrence of sub string:",str.count("L"))
print("ends with:", str.endswith("LD"))
print("find:",str.find('L'))
print("join:", ",".join(['1','2','3']))

#Lists
# Python lists are mutable type its mean we can modify its element after it created.
# The lists are ordered and mutable type.
# append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
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
#add()	Adds an element to the set
#clear()	Removes all the elements from the set
#copy()	Returns a copy of the set
#difference()	Returns a set containing the difference between two or more sets
#difference_update()	Removes the items in this set that are also included in another, specified set
#discard()	Remove the specified item
#intersection()	Returns a set, that is the intersection of two or more sets
#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	Returns whether two sets have a intersection or not
#issubset()	Returns whether another set contains this set or not
#issuperset()	Returns whether this set contains another set or not
#pop()	Removes an element from the set
#remove()	Removes the specified element
#symmetric_difference()	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()	Return a set containing the union of sets
#update()	Update the set with another set, or any other iterable
#setDays = {"Monday", "Tuesday", "Wednesday", "Thursday","Sunday"} 
#setDays.add("Friday")
#setDays.update(["Friday", "Saturday"]) # it accepts iterable ele
#setDays.discard("Tuesday"); # it will not throw error if item not found
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
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary

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

# input
ip = input("Enter a value or string:")
print(ip)

# files
# modes x-> create a new file, throws error if file name already exists, r->read, w->write, a->append, r+ ->read and write, w+ -> write and read, a+ -> append and read, rb -> read binary, wb,ab, rb+,wb+,ab+
file = open('index.html','w')
if file:
    print('file created')
else:
    print('file creation failed')
try:
    file.write('<html></html>')
finally:
    file.close()

fileAppend = open('index.html','a')
if file:
    try:
        fileAppend.write('<body></body>')
    finally:
        file.close()
else:
    print('did not find the file')

fileRead = open('index.html','r')
if fileRead:
    content = fileRead.read()
    print(content)
fileRead.close()

with open('index.html','r') as file:
    content = file.read()
    print(content)
# readline() to read each line file, 
#readlines() to read multiple lines in list
# tell() -> tells the pointer location
# seek() method which enables us to modify the file pointer position externally. offset([offset,from])

# modules

from modules.module import sum
print(sum(1,2))

from modules import module
print(module.sum(2,3))

from modules import module as test
print(test.sum(4,5))
# dir(package_name) -> print all the func, variables 
# reload(package) -> reimport the file

# Execption handling
try:
    1/0
except Exception:
    print(Exception)
else:
    print('print if succesfully done')
finally:
    print('it will be closed always')

# custom error
class ErrorInCode(Exception):      
    def __init__(self, data):      
        self.data = data      
    def __str__(self):      
        return repr(self.data)      
      
try:
    if(2<18):
        raise ErrorInCode(2000)
except ErrorInCode as ae:      
    print("Received error:", ae.data)

# time
import time
print(time.localtime(time.time()))

# Regular expression
# match,search, findall, split, sub
# span(): It returns the tuple containing the starting and end position of the match.
# string(): It returns a string passed into the function.
# group(): The part of the string is returned where the match is found.
import re 
reStr = "hello world"
print(re.match("h",reStr).span())

# send email
import smtplib    
sender_mail = 'sender@fromdomain.com'    
receivers_mail = ['reciever@todomain.com']    
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receivers_mail)    
try:    
   smtpObj = smtplib.SMTP('localhost')    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")  


# os module
# name, makdir(name), getcwd(), chdir(), rmdir(),
import os
print(os.name)

# magic methods
# __init__ :  The _init_ method is called after the instance of the class has been created but before it returned to the caller.
# __self__ : This function computes "informal" or a nicely printable string representation of an object and must return a string object.
# __repr__ : This function is called by the repr() built-in function to compute the "official" string representation of an object and returns a machine-readable representation of a type. The goal of the _repr_ is to be unambiguous
# __len__ : This function should return the length of an object.
# __call__ : We can make an object callable by adding the _call_ magic method, and it is another method that is not needed quite as often is _call_. If defined in a class, then that class can be called. But if it was a function, instance itself rather than modifying.

# __del__ : Just as _init_, which is a constructor method, _del_ is like a destructor. If you have opened a file in _init _, then _del_ can close it.

# __bytes__ : It offers to compute a byte-string representation of an object and should return a string object.

# __ge__ : This method gets invoked when >= operator is used and returns True or False.
# __neg__ : This function gets called for the unary operator.

# __ipow__ : This function gets called on the exponents with arguments. e.g. a**=b.

# __le__ : This function gets called on comparison using <= operator.

# _nonzero_ : This function returns the Boolean value of the object. It gets invoked when the bool (self) function is called.



 # Decorators
 # Decorators are one of the most helpful and powerful tools of Python. These are used to modify the behavior of the function. Decorators provide the flexibility to wrap another function to expand the working of wrapped function, without permanently modifying it.
def decor_fun(fun):
    fun()

@decor_fun 
def decor_fun_fun():
    print('hey')

# generators
def gen():
    yield 1
    yield 2
    yield 3

for each in gen():
    print(each)

# json
# loads => result will be in python dict
# dumps => result will be in json
# load => load(file_pointer)
# dump => dump(file_pointer)

import json
pyDict = { 'id': 1, 'name': 'test'}
print(type(pyDict))
jsObj = json.dumps(pyDict)
print(jsObj)
print(json.loads(jsObj))

# Multi processing
from multiprocessing import Process

def multi_process():
    print ('process started')  
if __name__ == '__main__':  
    p = Process(target=multi_process)  
    p.start()  
    p.join()

# OOPS concept

# Encapsulation
class Obj:
    def __init__(self,arg1):
        print(arg1)
        self.display('hey...')
    def display(self,arg1):
        print(arg1)
Obj(12)

# Inheritance
# multi level, multiple is supported

class subObj(Obj):
    def __init__(self):
        print('child')
subObj()
#overriding
class Animal:  
    def speak(self):  
        print("speaking")  
class Dog(Animal):  
    def speak(self):  
        print("Barking")  
d = Dog()  
d.speak()


# mysql connection

# from mysql import connector

# myDb = connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'password'
# )

# myDbCursor = myDb.cursor()
# myDbCursor.excute('Create database test')
# print(myDb)
# myDbCursor.execute("SHOW DATABASES")

# for x in myDbCursor:
#   print(x)