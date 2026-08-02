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

for i in range(symbol_location):
    n1 = n1 + a[i]

print(n1)