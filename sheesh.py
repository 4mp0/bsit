class user: #class = blueprint for variables, user = class name
    data: dict[str, int] = {}
    push: list[str, int] = []
    string: str = "" #string = variable, str = data type for variable, Hello = value
    integer: int = 0
    
def main(): #def = create function, main = function name, () = parameter
    
    def reg():
        userinput = input("input name: ") #userinput = variable, () = print before input
        user.string = userinput #user = calling declared class, string = calling the variable inside the class, (variable = input) = make variable same as the input
        userinput = input("input age: ")
        user.integer = userinput
        if len(userinput) != 0:
            user.push.append(user.string); user.push.append(user.integer)
        else:
            print("error")
    reg()             
    
    i = 0
    while i < len(user.push):
        if i == 0:        
            user.data["name"] = user.push[i]
        elif i == 1:            
            user.data["age"] = user.push[i]
        i += 1
    
    print(user.data) #user = calling declared class, string = calling the variable
main() # main() #calling declared function to run or start

