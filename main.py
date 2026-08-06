import calc

a = input("enter : ")
symbol_location = 0 
count = 0
n1 = ""
n2 = ""

for i in a:
    if i in "+-x*/÷×":
        symbol_location = count
    count += 1

n1 = int(a[:symbol_location])
n2 = int(a[symbol_location + 1:])
op = a[symbol_location]

if op in "+":
    print(calc.add(n1,n2))