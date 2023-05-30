def start_game():
    print("Welcome to Bandersnatch!")
    print("A Program inspired by Netflix Series Black Mirror : Bandersnatch")
    print("You find yourself in a mysterious room with two doors.")
    print("Which door do you choose? (1/2)")

    choice = input()

    if choice == "1":
        door_1()
    elif choice == "2":
        door_2()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def door_1():
    print("You open the first door and enter a dark hallway.")
    print("You see a flickering light at the end.")
    print("What do you do?")
    print("1. Walk towards the light.")
    print("2. Turn around and go back.")

    choice = input()

    if choice == "1":
        walk_towards_light()
    elif choice == "2":
        go_back()
    else:
        print("Invalid choice. Please try again.")
        door_1()

def door_2():
    print("You open the second door and step into a lush garden.")
    print("There is a path that leads deeper into the garden.")
    print("What do you do?")
    print("1. Follow the path.")
    print("2. Explore the surrounding area.")

    choice = input()

    if choice == "1":
        follow_path()
    elif choice == "2":
        explore_area()
    else:
        print("Invalid choice. Please try again.")
        door_2()

def walk_towards_light():
    print("As you walk towards the light, you hear a strange sound.")
    print("Suddenly, you find yourself transported to a different dimension. (Good Ending)")

def go_back():
    print("You decide to turn around and go back to the room. (Dumb Ending)")

def follow_path():
    print("You follow the path deeper into the garden.")
    print("You stumble upon a hidden treasure chest.")
    print("What do you do?")
    print("1. Open the chest.")
    print("2. Leave the chest and continue exploring.")

    choice = input()

    if choice == "1":
        open_chest()
    elif choice == "2":
        continue_exploring()
    else:
        print("Invalid choice. Please try again.")
        follow_path()

def explore_area():
    print("You explore the surrounding area and find a hidden cave.")
    print("The cave entrance looks dark and mysterious.")
    print("What do you do?")
    print("1. Enter the cave.")
    print("2. Stay outside and continue exploring.")

    choice = input()

    if choice == "1":
        print("Dax Eating You Alive The End (Bad Ending)")
        print("      ██████")
        print("      ██████")
        print("      ██████")
        print("      ██████")
        print("██████████████████")
        print("██████████████████")
        print("█████        █████")
        print("█████        █████")
        print("█████        █████")
        print("█████        █████")
        print("█████        █████")
    elif choice == "2":
        print("Coming Soon!")
        print("      ██████")
        print("      ██████")
        print("      ██████")
        print("      ██████")
        print("██████████████████")
        print("██████████████████")
        print("█████        █████")
        print("█████        █████")
        print("█████        █████")
        print("█████        █████")
        print("█████        █████")
    else:
        print("Invalid choice. Please try again.")
        explore_area()

def open_chest():
    print("You open the treasure chest and find a rare artifact.")
    print("The artifact grants you a special power.")
    print("Coming Soon!")

def continue_exploring():
    print("You decide to leave the chest/cave and continue exploring.")
    print("Coming Soon!")

start_game()
