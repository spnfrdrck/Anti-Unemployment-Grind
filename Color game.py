import random 

def colorgame():
    while True:  # Keep playing until the user decides to quit
        print("Welcome to the Color Game!")
        print("You pick a color. If the dice land on your color, you win based on how many dice match your choice!")

        bet = int(input("Place your bets ₱: "))
        print("Choose a color: Red, Green, White, Blue, Yellow, or Orange")
        user_choice = input("Enter your color choice: ").capitalize()  # Ensure capitalization matches list

        colors = ["Red", "Green", "White", "Blue", "Yellow", "Orange"]
        Roll1 = random.choice(colors)
        Roll2 = random.choice(colors)
        Roll3 = random.choice(colors)

        print(f"\n🎲 Dice 1 rolled: {Roll1}")
        print(f"🎲 Dice 2 rolled: {Roll2}")
        print(f"🎲 Dice 3 rolled: {Roll3}")

        # Count how many times the chosen color appears
        match_count = [Roll1, Roll2, Roll3].count(user_choice)

        # Determine winnings
        if match_count == 3:
            print("\n🎉 You won!!! You must have a lucky charm on you!")
            winnings = bet * 4
        elif match_count == 2:
            print("\n🎉 You won!!! Luck is really on your side!")
            winnings = bet * 3
        elif match_count == 1:
            print("\n🎉 You won!!! It must be your lucky day!")
            winnings = bet * 2
        else:
            print("\n😞 Aww, you lost. Luck wasn't on your side this time.")
            winnings = 0

        print(f"You won ₱{winnings}!")

        # Ask if the user wants to play again
        answer = input("Do you want to play again? (Y/N): ").lower()
        if answer == "n":
            print("Thanks for playing! Goodbye!")
            break  # Exit the loop

colorgame()  # Start the game
