import calc

a = input("enter : ") 1162534+1237123
symbol_location = 0 
count = 0
n1 = ""
n2 = ""

for i in a:
    if i in "+-x*/÷×":
        symbol_location = count
    count += 1

n1 = a[:symbol_location]     
n2 = a[symbol_location + 1:] 
 
