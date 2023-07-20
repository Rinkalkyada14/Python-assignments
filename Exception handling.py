


'''Error in Python can be of two types i.e. Syntax errors and Exceptions.
Errors are problems in a program due to which the program will stop the execution.
exceptions are raised when some internal events occur which change the normal flow of the program.

SyntaxError, TypeError, NameError, IndexError, KeyError, ValueError, AttributeError, IOError, ZeroDivisionError, ImportError,
'''

'''a = 1000
#if(a>2000)
#print("you areeligible to purchase ninja"
#try:
    x = a/0
    print(a)
#except ZeroDivisionError as p:
 #   print("exception caught")'''



'''def sync(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
 

sync(2, 3)
sync(3, 3)
sync(0,4)'''


'''try:
    raise NameError("Hi there")  
except NameError:
    print ("An exception")
    raise'''


'''def checkAge(age):  
    if age < 18:  
        raise Exception(" Age must be 18 or above. ")  
    else:  
        print(" Age is valid. ")  
  
try:  
    checkAge(12)  
except Exception as i:  
    print(" An error occurred: ", i) '''



'''class Error(Exception):
    pass

class PasswordSmallError(Error):
    pass

class PasswordLargeError(Error):
    pass

try:
    password = input("Enter a password")

    if len(password) < 6:
        raise PasswordSmallError("Password is short!")

    if len(password) > 15:
        raise PasswordLargeError("Password is long!")
	
except PasswordSmallError as ps:
    print(ps)

except PasswordLargeError as pl:
    print(pl)'''
