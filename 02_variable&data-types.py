"""
1. Variables & Data Types
What is a Variable?

A variable is used to store data in memory.

x = 10
name = "Gaurav"


Python automatically detects the data type.

Common Data Types
Type	           Example	          Description

int	                10	           Integer numbers
float	            3.14	       Decimal numbers
str	              "Python"	             Text
bool	          True, False	    Boolean values

✨Examples:-
age = 20
price = 99.99
language = "Python"
is_student = True

Type Checking & Conversion
type(age)          # Check type
int("10")          # Convert to integer
float("3.5")       # Convert to float
str(100)           # Convert to string

example:-
a = "44"
b = float(a)
t = type(b)
print(t)

#output:
<class 'float'>

1️⃣ Arithmetic Operators
Used for basic math.

Operator      Meaning	       Example	  Output
+	            Addition	    5 + 3	    8
-	           Subtraction	    5 - 3     	2
*	          Multiplication    5 * 3	    15
/      	        Division	    5 / 2	   2.5
//	          Floor Division    5 // 2	    2
%	        Modulus (remainder)	5 % 2	    1
**	            Power	        2 ** 3	    8

✨Examples:-
a = 10
b = 3
print(a + b)
print(a // b)
print(a ** b)

2️⃣ Comparison (Relational) Operators

Used to compare values. Result is True or False.

Operator	        Meaning	          Example
==	               Equal to	           5 == 5
!=	              Not equal to	       5 != 3
>	              Greater than	       5 > 3
<	               Less than	       3 < 5
>=	           Greater than or equal   5 >= 5
<=	            Less than or equal	   3 <= 5

✨Examples:-
x = 10
y = 20
print(x > y)
print(x != y)

3️⃣ Assignment Operators

Used to assign values.

Operator	       Meaning	        Example
=	               Assign	        x = 10
+=	             Add & assign	    x += 5
-=	           Subtract & assign	x -= 5
*=	           Multiply & assign	x *= 2
/=	             Divide & assign	x /= 2

Examples:-
x = 10
x += 5
print(x)

4️⃣ Logical Operators

Used in conditions. Think decision-making brain 🧠

Operator	         Meaning
and	           True if both conditions are true
or	           True if any condition is true
not	           Reverses result

✨Examples:-
age = 20
print(age > 18 and age < 25)
print(not age > 30)       
# """
# a = int(input("Enter number 1:")) 
# b = int(input("Enter number 2:")) 

# print("Sum of a+b:",a+b)

# a = input("Enter any type: ")
# print(type(a))

# a = int(input("Enter number 1: ")) 
# b = int(input("Enter number 2: ")) 

# print("a is greater than b is: ",a>b)

"""
....STRINGS....

a = "python programming"
print(a[0])          # First character
print(a[-1])         # Last character
print(a[0:6])       # Substring 'python'
print(a[7:])        # Substring 'programming'
print(a[:6])        # Substring 'python'
print(len(a))       # Length of string
print(a.upper())    # Uppercase
print(a.lower())    # Lowercase
print(a.replace("python", "java"))  # Replace substring
print("program" in a)  # Check substring presence   # True         
print("data" in a) # Check substring presence   # False


"""
