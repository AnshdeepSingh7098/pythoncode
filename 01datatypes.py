#DataType
# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:   	bytes, bytearray, memoryview
# None Type:	    NoneType

# type function
x=5  #declaring a variable x - it is a container for storing data values.  like 5 is value which is store in variable x.
print("1",type(x))  # this type function tell us the datatype of variable.

#str datatype
x = "Hello World"
print("2",x)
print("3",type(x)) #string

#int datatype
x=2
print("4",type(x))  #int

#float datatype
x=3.14
print("5",type(x))  #float

#complex datatype
x=1j
print("6",type(x))

#list datatype
x=["apple","banana"]
print("7",type(x))

#tuple datatype
x=("apple","cherry")
print("8",type(x))

x=range(6)
print(x)
print("9",type(x))

#dict datatype 
x={"name":"ansh","age":18}
print("10",type(x))

#set
x={"apple","cherry"}
print("11",type(x))

#frozenset
x=frozenset({"apple","cherry"})
print("12",type(x))

#bool datatype
x=True
print("13",type(x))

#bytes
x=b"hello"
print(x)
print("14",type(x))

# bytearray
x=bytearray(5)
print(x)
print("15",type(x))

#memoryview
x=memoryview(bytes(5))
print(x)
print("16",type(x))
 
#None datatype
x=None
print("17",type(x))