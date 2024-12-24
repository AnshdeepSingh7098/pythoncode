#Arithmetic operators
x = 5
y = 3
#addition
print(x + y)

#substraction
print(x - y)

#Multiplication
print(x * y)

#Division
print(x / y)

#modulus
print(x % y)

#exponential
print(x ** y)

#floor division
print(x // y)

#assingnment operators
# x=5
# x+=3
# x-=3
# x*=3
# x/=3
# x//=3
# x%=3
# x**=3
# x&=3
# x|=3
# x^=3
# x>>=3
# x<<=3
# x:=3

#comparision operators
# x==y
# x!=y
# x>=y
# x<=y
# x>y
# x<y

#logical operators
# x < 5 and  x < 10 Returns True if both statements are true
# x < 5 or x < 4  Returns True if one of the statements is true
# not(x < 5 and x < 10)Reverse the result, returns False if the result is true

#identity operators
# x is y  Returns True if both variables are the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# x is not y   	Returns True if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#Membership Operators
# x in y  Returns True if a sequence with the specified value is present in the object	
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list


# x not in y 	Returns True if a sequence with the specified value is not present in the object
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


# Bitwise Operators
# & 	AND	                    Sets each bit to 1 if both bits are 1	(x & y)	
# |  	OR	                    Sets each bit to 1 if one of two bits is 1	(x | y	)
# ^  	XOR                  	Sets each bit to 1 if only one of two bits is 1	(x ^ y)	
# ~ 	NOT	                    Inverts all the bits	(~x	)
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	(x << 2	)
# >>	Signed right shift   	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	(x >> 2)