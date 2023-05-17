import string
a = input("Text to convert: ")
shift = int(input("Numshifter to shift: "))
for each in a:
        x = string.ascii_uppercase.index(each)
        print(each,"is position", x, "+", shift, " = ", x+shift)
        print("More than A-Z shiftecomes", (x+shift) % 26, "=",string.ascii_uppercase[((x+shift)%26)] )

    
