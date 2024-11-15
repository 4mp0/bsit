
print("Hello World")
print(f"Hello {"World"}")

string = "String"
string: str = "String"

integer = 0
integer: int = 0

flt = 1.0
flt: float = 1.0

integer = flt
string = integer
flt = string

print(input("Type 'Hello' "))
print(input(f"Type 'Hello {"World"}' "))

tuples_data = ("Hello World", 0, 0.1)
tuple_data = str, int, float = ("Student", 0, 0.1)

list_data = ["Student", 0, 0.1]
list_data: list[str, int, float] = ["Student", 0, 0.1]

dict_data = {"Student", 0, 0.1}
dict_data: dict[str, int, float] = {"Student", 0, 0.1}

print("\n",tuple_data,list_data,dict_data)

if_sample1 = 1
if_sample2 = 0

if if_sample1 != if_sample2 and if_sample1 == 1:
    if_sample1 -= 1
    if if_sample1 == if_sample2 and if_sample1 != 1:
        print("\n",True)

list_data = ["Ampyc", 1, 0.1]
dict_data = {}

for items in range(len(list_data)):
    dict_data[f"Key{items}"] = list_data[items]
print("\n",dict_data,"\n")

i = 0
while i < len(dict_data):
    print(dict_data[f"Key{i}"])
    i += 1

def hello_world():
    print("Hello World")

def shout(arugment):
    print(arugment)
shout("\nHello!\n")

def shout(*args):
    print(args)
shout("arg1", "arg2")

def add(x, y):
    print("\n", x + y, "\n")
add(1, 2)

def func1():
    print("\nHello")

def func2():
    print("\nHi")

def func3():
    print("\nJyuu")

funcs: dict[str] = {"1":func1, "2":func2, "3":func3}
usrinput = input("input 1, 2, 3 ")
run = funcs.get(usrinput, "3")()