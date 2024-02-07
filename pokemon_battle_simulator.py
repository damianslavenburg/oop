from charmanderclass import Charmander


def main():
    charmander = Charmander(
        nickname= "Charmander",
    )
    game_running = True

    while game_running:
        print("1. Start the game")
        print("2. Quit the game")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Game started!")
            name = str(input("Give a name to your Charmander: "))
            charmander.nickname = name

            for i in range (10):
                charmander.battle_cry()
            changename = int(input('would you like to change the name of your charmander?, 1. Yes 2. No  '))
            if changename == 1:
                str(input('what is the name you would like tho give: '))
            elif changename == 2:
                game_running = True

        elif choice == "2":
            print("Game over!")
            quit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    