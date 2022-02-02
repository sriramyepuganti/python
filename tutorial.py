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