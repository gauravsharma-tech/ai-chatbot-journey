"""
🔝 Python Operator Precedence (High → Low)

Priority	 Operator(s)	         Meaning
1️⃣	              ()	           Parentheses
2️⃣	              **	          Exponentiation
3️⃣	              + -	         Unary plus, minus
4️⃣	            * / // %	Multiply, Divide, Floor, Mod
5️⃣	              + -	        Addition, Subtraction
6️⃣	              << >>	            Bitwise shifts
7️⃣	              &	                Bitwise AND
8️⃣	              ^	                Bitwise XOR
9️⃣	              `              	`
🔟	         == != > < >= <=	    Comparisons
1️⃣1️⃣	          not	             Logical NOT
1️⃣2️⃣	          and	             Logical AND
1️⃣3️⃣	          or	             Logical OR
1️⃣4️⃣	       = += -= *= /=         Assignment

✨Example demonstrating precedence:-
result = 3 + 5 * 2 ** 2 - (4 / 2)
# Step 1: Exponentiation    2 ** 2 = 4
# Step 2: Multiplication    5 * 4 = 20
# Step 3: Division          4 / 2 = 2.0
# Step 4: Addition          3 + 20 = 23
# Step 5: Subtraction       23 - 2.0 = 21.0
print(result)  # Output: 21.0

✨Remember: Use parentheses to control precedence and make code clearer!
Examples:-
a = 4 + 3 * 2
b = (4 + 3) * 2
print(a)  # Output: 10
print(b)  # Output: 14
print(not (a > b or a == 10))  # Output: True Reverses result

✨Examples:-
p = True
q = False
print(p and q)  # Output: False
print(p or q)   # Output: True

5️⃣ Bitwise Operators
Used to manipulate bits.
Operator	    Meaning	            Example
&	        Bitwise AND	        5 & 3
|	        Bitwise OR	        5 | 3 
^	        Bitwise XOR	        5 ^ 3
~	        Bitwise NOT	        ~5
<<	      Left Shift	        5 << 1
>>	      Right Shift	        5 >> 1

✨Examples:-
m = 5  # Binary: 0101
n = 3  # Binary: 0011
print(m & n)  # Output: 1  (Binary: 0001)
print(m | n)  # Output: 7  (Binary: 0111)
print(m ^ n)  # Output: 6  (Binary: 0110)
print(~m)     # Output: -6 (Binary: ...11111010)
print(m << 1) # Output: 10 (Binary: 1010)
print(m >> 1) # Output: 2  (Binary: 0010)

✨Examples:-
a = 12  # Binary: 1100
b = 5   # Binary: 0101
print(a & b)  # Output: 4  (Binary: 0100)
print(a | b)  # Output: 13 (Binary: 1101)
print(a ^ b)  # Output: 9  (Binary: 1001)
print(~a)     # Output: -13 (Binary: ...11110011)
print(a << 2) # Output: 48 (Binary: 110000)
print(a >> 2) # Output: 3  (Binary: 0011)
print(5 + 3 * 2 ** 2 - (4 / 2))  # Output: 10.0

"""