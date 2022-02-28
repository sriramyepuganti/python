# add two number
def add_num(a,b):
    return a + b
print("Add two number:", add_num(10,15))

# find the Maximum of these two numbers.
def max_num(a,b):
    return a if a > b else b
print("Large number:",max_num(10,15))

# factorial number
def facto_num(num):
    if(num == 0):
        return 1
    return num*facto_num(num-1)
print(facto_num(6))

# simple interest
def simple_interest(p=1000,t=1,r=12):
    return (p*t*r)/100
print('simple interest:',simple_interest(p=100000,r=24))


# compound interest 
def compound_intrst(p=1000,t=1,r=12):
    total = p * pow((1+r/100),t)
    return total - p
print("compound",compound_intrst(p=1200, t=2, r=5.4))

# count digit
def count_digit(num):
    if(num == 0 ):
        return 1
    count = 0
    while(num !=0):
        num = num/10
        count += 1
    return count

# Armstrong Number

def is_armstrong_num(num):
    count = count_digit(num)
    temp = num
    total = 0
    while(temp!=0):
        rem = temp%10
        temp/=10
        total+=pow(rem,count)
    return num == total
print("is armstrong number",is_armstrong_num(1634))
    
# area of circle
def area_of_circle(radius):
    return (3.14 * pow(radius,2))
print("area of circle", area_of_circle(10))

# print prime numbers in interval
def print_prime(start, end):
    result = []
    for val in range(start,end):
        for i in range(2,val):
            if(val%i == 0):
                break
        else:
            result.append(val)
    return result

print("print prime numbers", print_prime(2,100))

# print ASCII Value of a character
print("ascii value:",ord('a'))

# sum of array ele
listExm = [10,4,5,3,6,3,5]
def array_sum(array):
    total = 0
    for x in array:
        total+=x
    return total
print("sum of array elements:",array_sum(listExm)) # use sum(array_list)

# largest element
largestInList = 0
for x in range(len(listExm)):
    if listExm[x] > largestInList:
        largestInList = listExm[x]
print('lrgest in list:',largestInList)

# palindrome
string = 'malayalame'
def checkPalindrome(stri):
    temp = stri[::-1]
    for x in range(len(stri)):
        if stri[x] != temp[x]:
            break
    else:
        print('palidrome')
checkPalindrome(string)