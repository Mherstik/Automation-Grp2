import string
userText = input("Text to convert: ")
shift = int(input("Numshifter to shift: "))
for each in userText:
        x = string.ascii_uppercase.index(each)
        print(each,"is position", x, "+", shift, " = ", x+shift)
        print("More than A-Z shiftecomes", (x+shift) % 26, "=",string.ascii_uppercase[((x+shift)%26)] )

    
