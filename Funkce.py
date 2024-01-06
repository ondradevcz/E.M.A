# To-do List

from tinydb import TinyDB, Query
db2 = TinyDB('to-do.list.json')
TDLDatabase = Query()
import random
import time


# To do list

def Launch_ToDoListApp():
    while True:
        command = input("What do you wish to do?\nYou can delete or make a new note, to end just type 'end'\nType here: ")

        # COMMANDS
        t_delete = ("delete", "Delete", "erase")
        t_new_note = ("new note", "newnote", "new", "New", "New note", "New Note", "Newnote")
        t_end = ("end", "End", "Ending", "ending", "Stop", "stop")

        if any(action in command for action in t_new_note):
            title = input("Enter the title of the note: ")
            content = input("Enter the content of the note: ")
            db2.insert({"title": title, "content": content})
            print("Note created!")
        elif any(action in command for action in t_delete):
            all_notes = db2.search(TDLDatabase.title.exists())
            if all_notes:
                print(all_notes)
                title = input("Enter the title of the note you want to delete: ")
                db2.remove(TDLDatabase.title == title)
                print("Deleted")
            else:
                print("No notes to delete.")
        elif any(action in command for action in t_end):
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")


def PasswordGenerator():
    while True:
        characters_count = input("Napiš kolik znaků má mít tvoje nové heslo: ")

        lowercase_letters = "qwertyuiopasdfghjklzxcvbnm"
        uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
        numbers = "123456789"

        letters = lowercase_letters + uppercase_letters + numbers
        l_letters = list(letters)

        password = ""

        for i in range(int(characters_count)):
            random_letter = random.choice(l_letters)
            password += random_letter

        print(password)


def BMI_Calculator():
    # variables:
    weight = input("What is your current weight? In KG please.  \n Write here: ")
    height = input("What is your current height? Please write like this - metres, centimetres (E.g.: 1.75) \n Write here: ")

    f_weight = float(weight)
    f_height = float(height)

    BMI = round((f_weight / f_height) / f_height, 1)

    weight_status = ""

    if BMI <= 18.5:
      weight_status = "you might be underweight."
    elif BMI > 18.5 and BMI <= 25:
      weight_status = "you have a normal weight."
    elif BMI >= 25 and BMI <= 30:
      weight_status = "you might be overweight."
    elif BMI >= 30 and BMI <= 35:
      weight_status = "you might have obesity, you should consult this with your doctor."
    elif BMI > 40:
      weight_status = "you're heavily obese, seek professional help immediately."

    print(f"Your BMI is {BMI}, {weight_status}")


def SimpleTimer():
    timer = 0
    starttime = time.time()
    print("TIMER STARTS")
    while True:
      timer += 1
      print(timer)
      # Remove the Time taken by code to execute
      time.sleep(1.0 - ((time.time() - starttime) % 1.0))

def RockPaperScissors():
    types_of_guesses = ('Rock', 'Paper', 'Scissors')

    while True:
        guess = input('Type your guess  \n Rock, Paper or Scissors?  \n       Type here: ')

        if guess.lower() == "end":
            print('Thanks for playing with me!')
            break
        elif guess not in types_of_guesses:
            print('Invalid guess')
        else:
            computer_guess = random.choice(types_of_guesses)

            if guess == computer_guess:
                print("It's a tie!")
            elif (guess == "Rock" and computer_guess == "Scissors") or \
                    (guess == "Scissors" and computer_guess == "Paper") or \
                    (guess == "Paper" and computer_guess == "Rock"):
                print("You win!")
            else:
                print('You lost')
