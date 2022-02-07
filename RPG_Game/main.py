from time import sleep
from game_classes import *

def main():
    character = input('What is your name?: ')
    Welcome = f'Welcome, {character}. It really is too bad how you got here. The scent of the Deathless still lingers on your skin.\n'
    print(Welcome)
    sleep(2)
    magic_number = 0
    
    while magic_number == 0:
        class_message = 'What were you in your past life? Before your life was stricken from the waking world?\n'
        print(class_message)
        class_choice = input(' 1. Cleric \n 2. Knight \n 3. Mage \n 4. Thief \n 5. Hunter \n\n Select a number: ')
        if class_choice == '1':
            characterType = cleric()
            magic_number = 1
        elif class_choice == '2':
            characterType = knight()
            magic_number = 1
        elif class_choice == '3':
            characterType = mage()
            magic_number = 1
        elif class_choice == '4':
            characterType = thief()
            magic_number = 1
        elif class_choice == '5':
            characterType = hunter()
            magic_number = 1
        else:
            print('Invalid choice. Please select a number')
            sleep(2)
    
    print(f'Well, well, well. A {characterType}?')
    print(f'Interesting. Well, Sir {character} the {characterType.name}. Your quest begins here. You are charged with the duties as many have before you. You are a tarnashed relic from a world you no lonmger belong. You now, are a fleeting spark. Bring light to the darkness, tiny spark.')

main()