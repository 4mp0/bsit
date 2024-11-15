
x = input("input number:\n")
operators = input("input operator:\n")
y = input("input number:\n")

if operators == "+":
    sumOf=int(x)+int(y)
    print(sumOf)
if operators == "-":
    sumOf=int(x)+int(y)
    print(sumOf)

def main(sumOfPD):
    global sumOf
    operators = input("input operator:\n")
    y = input("input number:\n")
    if operators == "+":
        sumOfPD = int(sumOf)+int(y)
        sumOf=sumOfPD
        print(sumOfPD)
        main(sumOf)
    if operators == "-":
        sumOfPD = int(sumOf)-int(y)
        sumOf=sumOfPD
        print(sumOfPD)
        main(sumOf)
    if operators == "*":
        sumOfPD = int(sumOf)*int(y)
        sumOf=sumOfPD
        print(sumOfPD)
        main(sumOf)
    if operators == "/":
        sumOfPD = int(sumOf)/int(y)
        sumOf=sumOfPD
        print(sumOfPD)
        main(sumOf)
main(0)
