# ============================================================
# Python Final Project 2026
# Name: Dash Diggs
# Date: 5/7/26
# Project Title: Python Final Project 2026
# Description: (Write 1-2 sentences explaining what your program does)
# ============================================================


# ---- SECTION 1: Setup / Variables ----
playerName = input("What is your name?: ")



# ---- SECTION 2: Welcome Message ----
print(f"Hello,", playerName)

print("Welcome!")
print("----------------------------")



# ---- SECTION 3: Get Input from User ----
race = input("What is your race?: ")
age = int(input("How old are you?: "))
year = float(input("What year is it?: "))




# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.

if race == "Goblin":
    print("You stupid green skin")
elif race ==  "Dragonborn":
    print("You're the best race")
else:
    print("I hope you die")
if age >= 26:
    print("Damn you old")



# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.

print("----------------------------")
print("Thanks for using my program!")
