from charmanderclass import Charmander
from charmanderclass import Charmander

def main():
    charmander = Charmander()
    game_running = True

    while game_running:
        print("1. Start the game")
        print("2. Give a name to Charmander")
        print("3. Charmander does its battle cry")
        print("4. Quit the game")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Game started!")
        elif choice == "2":
            name = input("Enter a name for Charmander: ")
            charmander.set_name(name)
            print("Name set to", charmander.get_name())
        elif choice == "3":
            charmander.battle_cry(10)
        elif choice == "4":
            game_running = False
            print("Game over!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    