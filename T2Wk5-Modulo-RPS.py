
rock = 1
paper = 2
scissors = 3

a = input("Give me 1, 2, 3")
b = input("Give me 1, 2, 3")

print((rock - paper) % 3) # p2 wins
print((rock - scissors) % 3) #p1 wins
print((rock - rock) % 3) # tie

print((scissors - rock) % 3) #p2 wins
print((scissors - paper) % 3) #p1 wins

if ((a - b) % 3) == 2:
    print("player 2 wins")
elif ((a - b) % 3) == 1:
    print("player 1 wins")
else:
    print("It's a tie")
    

