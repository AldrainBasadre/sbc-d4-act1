import random
while True:
    print("please Enter the Number your betting at.")

    first = int(input("please enter the first number: "))
    second = int(input("please enter the second number: "))
    third = int(input("please enter the third number: "))

    Lfnum,Lsnum,Ltnum = random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)

    mylist = [first,second,third]
    lotolist = [Lfnum,Lsnum,Ltnum]

    print("your number are: ",mylist)
    print("And the Result are:",lotolist)

    if first == Lfnum and second == Lsnum and third == Ltnum:
        print("Jackpot".upper())
    elif all(num in lotolist for num in mylist) and len(set(mylist)) == len(mylist):
        print("you partially win some rewards")
    else:
        print("Better Luck next time")
    play_again = input("Wanna bet again? (yes/no): ").strip().upper()
    if play_again != 'yes':
        break

print("Thank you for playing!")