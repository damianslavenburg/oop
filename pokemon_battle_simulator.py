from models import *

def main():
    charmander = Charmander(
        nickname= "Charmander",
    )
    trainer = Trainer(
        name = "name", 
        belt = []
    )
    
    Trainers = {

    }

    game_running = True

    while game_running:

    # <----------- The player start the game ----------->      
        
        print("1. Start the game")
        print("2. Quit the game")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Game started!")

    # <---------- The player gives a name to the first Trainer ---------->

            Trainer1 = trainer.name = input("Please choose a name for the first tainer\n" )
            

    # <---------- The player gives a name to the second Trainer ---------->


            Trainer2 = trainer.name = input("Please choose a name for the second tainer\n" )


    # <--------- The player gives a name to a charmander ---------> 
            
            name = str(input("Give a name to your Charmander: "))
            charmander.nickname = name

    # <------ The charmander does its battle cry for ten times ------>
            
            for i in range (10):
                charmander.battle_cry()

    # <------- The player can give a new name to the same charmander -------->

            changename = int(input('would you like to change the name of your charmander?, 1. Yes 2. No  '))
            if changename == 1:
                str(input('what is the name you would like tho give: '))
            elif changename == 2:
                game_running = True

    # <------ The player can choose to quit the game or continue ------>
                
        elif choice == "2":
            print("Game over!")
            quit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    