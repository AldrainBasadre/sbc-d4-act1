from random import randint
while True:
    def get_choice_name(choice):
        return "kulob" if choice else "hayang"

    me = int(input("ENTER 0 for HAYANG or 1 for KULOB: "))
    c2,c3 = randint(0,1),randint(0,1)

    choices = [me, c2, c3]
    names = ["Me", "C2", "C3"]

    for name, choice in zip(names, choices):
        print(f"{name}: {get_choice_name(choice)}")


    if me != c2 and me != c3:
        print("you win")
    elif c2 != me and c2 != c3:
        print("c2 win")
    elif c3 != me and c3 != c2:
        print("c3 win")
    else:
        print("draw")
    again = input("Wanna Play again? (yes/no): ").strip()
    if again != 'yes':
        break

print("Thank you for playing!")
