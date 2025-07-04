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
 
To start the game, set your goal to the number of points you aim to reach. 
Over or equal to 5, because less than 5 will be way too easy. Then answer 
the questions, if you get it right you get one step closer to reaching your 
goal, but if you get it wrong you will have to play more rounds to reach it. 
              
At the end it'll show you how many rounds you've played, including the 
correct answers if you got any wrong, make sure to get them right though...😗
              
          
Your aim is to try to reach your goal with no wrong answer.
          
 Good luck!😉
""")


# Main Routine Starts here
# Initialise game variables
user_score = 0
rounds_played = 0
correct_answers = 0


history = []



# Main Routine
# Show title of game / introduction
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


# Check users enter a integer more than / equal to 5
print()
game_goal = int_checker()

# Game loop starts here
# Play multiple rounds until the user has reached their game goal
while user_score < game_goal:

    if game_goal == "game goal":
        mode = "game goal"
        game_goal = 5

        # Start of round loop
        # generating questions
    num_one = random.randint(0,9)
    num_two = random.randint(0,9)
    math_symbols = ["plus"]

        # structureing the questions so it functions so it make sense for the user
    answers = num_one + num_two
    user_input = input(str(num_one) + "+" + str(num_two) + "=")
    user_input = int(user_input)

        # if user input is the correct answer then show user is right
    if (user_input == answers):
        print("Yay, you got it right😁")
        correct_answers += 1
        current_answers = [str(num_one) + "+" + str(num_two), answers]
        history.append(current_answers)

        # if incorrect answer is put then show user they got it wrong
    else:
        print("Aw naur, you got it wrong😭")
        current_answers = [str(num_one) + "+" + str(num_two), answers]
        history.append(current_answers)


    # Rounds increase until reached game goal if not
    # reached game goal then continue increasing rounds
    rounds_played += 1


    if correct_answers >= game_goal:
        break
        

# Game loop ends here
# Show user they finished game
make_statement("Game Over", "🏁")

# Show user they have reached their game goal
print()
if correct_answers >= game_goal:
    make_statement("You made it to your goal", "👍")
    print(f"you played {rounds_played} rounds")


# Game History / Statistics area
print("*** Game History ****")

for item in history:
    print(item)
