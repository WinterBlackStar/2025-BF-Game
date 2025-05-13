import random

# Initialise rounds points
quiz_quetsion = 0
double_user = "no"

# Roll the dice for the user and note if they got a double
quiz_quetsion = random.randint(1, 6)


# Roll the dice for the computer
quiz_quetsion = random.randint(1, 6)

# Update the user /  computer points


# output the results
print("\ninitial points")
print(f"question 1:     {quiz_quetsion}\t| Roll 2:  \t| Total: ")
print(f"computer - Roll 1:  \t| Roll 2:  \t| Total: ")

# let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win, you will earn double points")
