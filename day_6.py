#swith case
match =5
day=6
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tueseday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")


#While loop
a=9
while(a>0):
    print(a)
    a-=1

#guess the secrate number 
a = 5
v = int(input("Enter your guess: "))
while v != a:
    print("Try again")
    v = int(input("Enter your guess again: "))
print("You guessed it right 🎉")
