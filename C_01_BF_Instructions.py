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

# Display instructions
def instructions():
        print("""
 
 *** Instructions ***
 
To begin, choose the level of the questions and either customise 
the game parameters or go with the default game (where the 
level starts from level 1 and increases).
          
Then choose how many rounds you'd like to play <enter> for 
infinite mode.
          
Your goal is to try to answer all the questions without 
losing any rounds.
          
 Good luck!
""")


# Main routine
print()
print("➕➖✖️ ➗ Basic Facts➕➖✖️ ➗")
print()

# ask the user if they want to see instructions and display
# them if requested
want_instructions = string_checker("Do you want to see the instructions?")

# check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print()
print("program continues")
