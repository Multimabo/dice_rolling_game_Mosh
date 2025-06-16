import random

while True:
    # Ask: roll the dice?
    choice = input("Roll the dice? (y/n): ").strip().lower()
    # If user enters y
    if choice == 'y':
        # Generate two random numbers between 1 and 6
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        # Print the results
        print(f"You rolled a {die1} and a {die2}.")
    # If user enters n
    elif choice == 'n':
        #   Print thank you message
        print("Thank you for playing!")
        # Terminate the program
        break
    # Else
    else:
        #   Print invalid choice
        print("Invalid choic!")