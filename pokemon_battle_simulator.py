
from charmanderclass import Charmander

def main():
    charmander = Charmander()
    game_running = True

    while game_running:
        print("1. Start the game")
        print("2. Quit the game")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter a name for your Charmander: ")
            charmander.set_name(name)

            for _ in range(10):
                charmander.battle_cry()

        elif choice == "2":
            game_running = False
            print("Quitting the game...")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()