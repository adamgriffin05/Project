def show_menu():
    the_input = int(input(f"Enter choice: \n"
                          f"1 for addition \n"
                          f"2 for subtraction \n"
                          f"3 for division \n"
                          f"4 for multiplication \n"
                          f"5 to quit.\n"))
    if the_input not in [1, 2, 3, 4, 5]:
        print("Invalid input.")
        return 5
    return choice


print("Welcome to my calculator app")
choice = show_menu()
while choice in [1, 2, 3, 4]:
    numb1 = int(input("Enter your first number\n"))
    numb2 = int(input("Enter your second number\n"))
    if choice == 1:
        my_sum = numb1 + numb2
        print(numb1, "+", numb2, "=", my_sum)
    elif choice == 2:
        my_sum = numb1 - numb2
        print(numb1, "-", numb2, "=", my_sum)
    elif choice == 3:
        my_sum = numb1 / numb2
        print(numb1, "/", numb2, "=", my_sum)
    elif choice == 4:
        my_sum = numb1 * numb2
        print(numb1, "*", numb2, "=", my_sum)
    choice = show_menu()