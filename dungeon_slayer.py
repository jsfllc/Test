"""
This game is a text based game that will run users through a series of events.
The purpose of this game is to, successfully, get through all of the events and reach the
amulet of time and space.
"""

import sys


class RunGame:

    def __init__(self):
        self.initial_start()

    def initial_start(self):

        print("Hello, young traveler. "
              "I am the voice of reason to help you during your quest.")

        print("\nYou enter a dungeon and see two paths.")
        print("The path on your left is well lit, but has water that is waist high.")
        print("The path on your right is dark, but seems to be quite dry.")

        while True:
            first_choice = input("\nPlease pick your starting direction (L/R): ").upper()

            if first_choice == "L":
                print("You have chosen the path that contains water, be weary of the dungeon"
                      " crocodiles.")
                self.water_path()

            elif first_choice == "R":
                print("You have chosen the path of darkness, be weary of dungeon bats.")
                self.dark_path()

            else:
                print("please enter either 'L' or 'R'.")

    def water_path(self):
        print("\nYou move through the water slowly only to see a right turn ahead.")

        while True:
            water_choice_options = input("\nDo you take the path on the right (R) or continue straight (S) "
                                         "(R/S)?: ").upper()
            if water_choice_options == "R":
                print("You see a long corridor with a light at the end. You continue "
                      "toward the light.")
                self.battle_room()

            elif water_choice_options == "S":
                print("You meet your demise at the hands of a dungeon crocodile.")
                self.retry()

            else:
                print("Please enter either 'R' or 'S'.")

    def dark_path(self):
        print("\nYou continue down the dark path, ahead you see a corridor to your left.")
        dark_choice_option = input("\nDo you continue straight down the dark corridor (S) or do you turn left down "
                                   "the corridor (L) (L/S)?: ").upper()
        while True:
            if dark_choice_option == "L":
                print("You see a long corridor with a light at the end. You continue "
                      "toward the light.")
                self.battle_room()

            elif dark_choice_option == "S":
                print("You have met you demise at the hands of a half man, half bat hybrid.")
                self.retry()

            else:
                print("Please enter either 'L' or 'S'.")

    def battle_room(self):
        print("\nYou follow the light and enter a large room.")
        print("Upon entering the room you are met by three large enemies.")
        print("Before battle you see a large sword and shield.")
        while True:
            battle_room_options = input("\nDo you pick the sword and shield up and fight (F) or do you run (R) "
                                        "(F/R)?: ").upper()
            if battle_room_options == "F":
                print("Your training has paid off, you have defeated the enemies.")
                self.final_room()

            elif battle_room_options == "R":
                print("You're slower than you look, the enemies make waste of you.")
                self.retry()

            else:
                print("Please enter either 'F' or 'R'.")

    def final_room(self):
        print("\nAfter defeating the enemies, you see a large set of wooden doors.")
        print("You push through the doors to see the amulet of time before you on a stone podium.")
        print("As you step closer you see the dark wizard who guards the amulet of time.")

        while True:
            final_battle = input("\nDo you choose to initiate battle (B) with the wizard or do you try and reason (R) "
                                 "with him (F/R)?: ").upper()

            if final_battle == "F":
                print("You come to battle with only a sword and shield and actually expected to win? Regardless you "
                      "are now a toad.")
                self.retry()

            elif final_battle == "R":
                print("Turns out the wizard was a nice guy and you two exchange contact information to catch lunch "
                      "later, he gives you the amulet as a gift.")
                self.final_decision()

            else:
                print("Please enter either 'F' or 'R'.")

    def final_decision(self):
        last_decision = input("You have now collected the amulet and even gained a 'bestie' do you choose to use the "
                              "amulet of time (U) or do you choose to 'call it a day' (Q) (U/Q)?: ").upper()

        if last_decision == "U":
            print("\nFool! You do not know how to use the amulet... of... ti...")
            self.initial_start()

        elif last_decision == "Q":
            print("\nYou deserve a day off, thank you for completing the quest. Happy travels!")
            sys.exit()

        else:
            print("Please enter either 'U' or 'Q'.")

    @staticmethod
    def retry():
        while True:
            restart = input("\nWould you like to begin your quest again (Y/N)?: ").upper()
            if restart == "Y":
                RunGame()
            elif restart == "N":
                print("Thanks for playing!")
                sys.exit()
            else:
                print("Please enter either 'Y' or 'N'.")


if __name__ == "__main__":
    RunGame()
