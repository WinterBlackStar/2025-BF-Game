import random

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


def mode_selection(question, valid_ans=("easy")):

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


def int_checker():
    """Check user enter an integer more than / equal to 5"""

    error = "Please enter an integer more than / equal to 5."

    while True:
        try:
            response = int(input("What's your Game Goal?"))

            if response < 5:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def make_statement(statement, decoration):
    """Adds emoji / additional characters to the start and end of heading"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")
# Display instructions

def instructions():
        print("""
 
 *** Instructions ***
 
To begin, choose the level of the questions easy (e),
medium (m), hard (h), easy has plus and minus, 
medium has times and hard has divition questions.
              
Then set game goal to the number of points you aim to reach (over 13).
          
Your goal is to try to reach or goal.
          
 Good luck!
""")


# Main Routine Starts here
# Initialise game variables
# At the start of the game, user score are zero
user_score = 0
rounds_played = 0
correct_answers = 0
rounds_won = 0


history = []



# Main Routine
print()
print("➕➖✖️ ➗ Basic Facts➕➖✖️ ➗")
print()

print("😄😄😄Welcome y'all to the Basic Facts Quiz😄😄😄")

# ask the user if they want to see instructions and display
# them if requested
want_instructions = string_checker("Do you want to see the instructions?")

# check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()


# Display Mode selection

print("\nenter (e) for easy mode")
mode_selection = input("\nwhat mode would you like?")


    # if user chooses easy, display question

if mode_selection =="e":
        print("you selected e")


print()
game_goal = int_checker()

# Game loop starts here
# Play multiple rounds until a winner has been found
while user_score < game_goal:

    if game_goal == "game goal":
        mode = "game goal"
        game_goal = 5

    # Start of round loop
 # Display questions for easy mode
    
    if mode_selection == "e":

        # generating questions
        num_one = random.randint(0,9)
        num_two = random.randint(0,9)
        math_symbols = ["plus"]

        if random.choice(math_symbols) == "plus":
                answers = num_one + num_two
                user_input = input(str(num_one) + "+" + str(num_two) + "=")
                user_input = int(user_input)

                if (user_input == answers):
                    print("Yay you got it right😁")
                    correct_answers += 1
                    current_answers = [str(num_one) + "+" + str(num_two), answers]


                else:
                    print("Aw naur, you got it wrong😭")
                current_answers = [str(num_one) + "+" + str(num_two), answers]
                history.append(current_answers)



    # Outside rounds loop - Update game goal
        rounds_played += 1


        if correct_answers >= game_goal:
            break
        
    if user_input == "xxx":
        break


make_statement("Game Over", "🏁")

# Game loop ends here
print()
if correct_answers >= game_goal:
    make_statement("You made it to your goal", "👍")
    print(f"you played {rounds_played} rounds")


# Game History / Statistics area
print("*** Game History ****")

for item in history:
    print(item)
