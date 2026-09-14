print("Hello world!")
name = input("Whats your name? ")
print(f"hello {name}!")

while True:
    choice = int(input("""(1) About me
(2) My goals
(3) College of choice
(4) Exit
: """))
    if choice == 1:
        print("I am empathetic.")
    elif choice == 2:
        print("I want to live life according to the commands of Allah")
    elif choice == 3:
        print("I will go to Yale by the will of Allah.")
    elif choice == 4:
        print("GoodBye!")
        break
    else:
        print("Please choose something in the list.")