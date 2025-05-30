import math
import random

random_num = random.randint(1, 10)


# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
    
            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item [0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def mode_selection(question, valid_ans=("easy", "medium", "hard")):

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
    
            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item [0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)
    
            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response
            
        except ValueError:
            print(error)


# Display instructions

def instructions():
        print("""
 
 *** Instructions ***
 
To begin, choose the level of the questions easy (e),
medium (m), hard (h), easy has plus and minus, 
medium has times and hard has divition questions.
          
Then choose how many rounds you'd like to play (push <enter> for 
infinite mode).
          
Your goal is to try to answer all the questions without 
losing any rounds.
          
 Good luck!
""")

# calculate easy mode questions

# Main Routine Starts here
# Initialise game variables
mode = "regular"
rounds_played = 1

# Main Routine
print()
print("➕➖✖️ ➗ Basic Facts➕➖✖️ ➗")
print()

# ask the user if they want to see instructions and display
# them if requested
want_instructions = string_checker("Do you want to see the instructions?")

# check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()


# Display Mode selection

print("\nenter mode selection easy (e), medium (m), hard (h)")
mode_selection = input("\nwhat mode would you like?")


    # if user chooses easy, display questio
    
if mode_selection =="e":
        print("you selected e")

    # if user chooses medium, display question
elif mode_selection =="m":
        print("you selected m")

    # if user chooses hard, display question
elif mode_selection =="h":
        print("you selected h")


# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for inifinte mode: ")


if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Round headings
    if mode == "infinite":
        rounds_heading = f"\n000 rounds {rounds_played + 1} (Infinite Mode) 000"
        # if users are in infinite mode, increase number of rounds!
        num_rounds += 1
    else:
        rounds_heading = f"\n 💿💿💿 round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

# get user choice
    user_choice = string_checker("Choose:", bf_list)
    print("you chose", user_choice)

# if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

# Game loop ends here

# Game History / Statistics area

