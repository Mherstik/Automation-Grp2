import string
a = input("letter: ")
b = int(input("Number: "))
for each in a:
        x = string.ascii_uppercase.index(each)
        print(each,"is position", x, "+", b, " = ", x+b)
        print("More than A-Z becomes", (x+b) % 26, "=",string.ascii_uppercase[((x+b)%26)] )

    
