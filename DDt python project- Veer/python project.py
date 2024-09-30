import random
import json
import time

# ANSI escape code for text colors
ANSI_RED = "\033[91m"
ANSI_GREEN = "\033[92m"
ANSI_RESET = "\033[0m"
ANSI_BackgroundGreen = "\u001b[42m"
ANSI_BackgroundRed  = "\u001b[41m"
ANSI_CYAN = "\u001b[36m"
ANSI_MAGENTA = "\u001b[35m"
ANSI_YELLOW = "\u001b[33m"
def clear_screen():
    # Function to clear the console screen
    print("\033c", end='')

clear_screen()

#display the ASCII art with time affect

print(rf"""{ANSI_CYAN}

                                                                  
 _____    _____   _____        _____    _     _  _______  _______ 
(_____)  (_____) (_____)      (_____)  (_)   (_)(_______)(_______)
(_)__(_)(_)___(_)(_)__(_)    (_)   (_) (_)   (_)   (_)       _(_) 
(_____) (_______)(_____)     (_)   (_) (_)   (_)   (_)     _(_)   
( ) ( ) (_)   (_)(_)         (_)___(_) (_)___(_) __(_)__  (_)____ 
(_)  (_)(_)   (_)(_)          (___(__)  (_____) (_______)(_______)
                                    (_)                           
                                                                                
                                                                                                      
{ANSI_RESET}""")

# Animation delay before the quiz starts (2 seconds)
time.sleep(1)

# Display bouncing animation for "RAP QUIZ"
print(rf"""{ANSI_MAGENTA}

   ___  __  __       _   __   ____   ____   ___         ___    ___    ___    __  ___   ___    ___ 
  / _ ) \ \/ /      | | / /  / __/  / __/  / _ \       / _ \  / _ |  / _ \  /  |/  /  / _ |  / _ \
 / _  |  \  /       | |/ /  / _/   / _/   / , _/      / ___/ / __ | / , _/ / /|_/ /  / __ | / , _/  
/____/   /_/        |___/  /___/  /___/  /_/|_|      /_/    /_/ |_|/_/|_| /_/  /_/  /_/ |_|/_/|_|  
                                                                                                  

                           
{ANSI_RESET}""")
time.sleep(2)

clear_screen()

print("""
========================
Welcome to the Rap Quiz!
========================
      """)
print("""
Choose your level:
""")
print(f"1 - {ANSI_BackgroundGreen}Level 1 (Easy){ANSI_RESET}")
print(f"2 - {ANSI_BackgroundRed}Level 2 (Advanced){ANSI_RESET}")

# The rest of the code remains the same.


level_choice = input("Enter the level number (1 or 2): ")

if level_choice == "1":
    file_name = "rap_quiz_level1.txt"
    level_name = "Level 1 (Easy)"
elif level_choice == "2":
    file_name = "rap_quiz_level2.txt"
    level_name = "Level 2 (Advanced)"
else:
    print(f"{ANSI_RED}Invalid level choice. Please choose 1 or 2.{ANSI_RESET}")
    exit()

print(f"\nYou have chosen {ANSI_GREEN}{level_name}{ANSI_RESET}.\n")

# Read the questions and answers from the chosen level JSON file
with open(file_name, "r") as file:
    questions_data = json.load(file)

# Shuffle the questions to randomize the order
random.shuffle(questions_data)

# Initialize score
score = 0

# Loop through each question and present it to the user
for question_data in questions_data:
    print(question_data["question"])
    options = question_data["options"]
    for i, option in enumerate(options):
        print(f"{chr(65 + i)}) {option}")

    answer = input("Enter your answer (A, B, C, or D): ").upper()

    correct_answer = question_data["answer"]

    if answer == correct_answer:
        print(f"{ANSI_GREEN}Correct!{ANSI_RESET}")
        score += 1
    else:
        print(f"{ANSI_RED}Incorrect! The correct answer is {correct_answer}.{ANSI_RESET}")

    print()

# Quiz summary
print("Quiz Summary:")
print(f"You answered {ANSI_GREEN}{score}{ANSI_RESET} out of {ANSI_GREEN}{len(questions_data)}{ANSI_RESET} questions correctly.")
percentage = (score / len(questions_data)) * 100
print("Your score:", f"{ANSI_GREEN}{percentage:.2f}%{ANSI_RESET}")

print(rf"""{ANSI_RED}

  __    _         ___    __        ___   __  
 / _   /_|  /|/| (_     /  ) (  / (_    /__) 
(__)  (  | /   | /__   (__/  |_/  /__  / (   
                                             
                                                                                                                               
                                                                                                      
{ANSI_RESET}""")
