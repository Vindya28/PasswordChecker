# PasswordChecker
Check the strength of your password on a scale of 7. 7 being the strongest and 1 being the weakest

This project is a Password Strength Checker written in Python. It evaluates the strength of a given password and provides a score out of 7 based on various criteria such as length, character variety, and common password lists.

The Password Strength Checker operates in several steps to evaluate the strength of a password:

User Input: The program prompts the user to enter a password.

Character Type Checks: The program checks if the password contains uppercase letters, lowercase letters, special characters, and digits.

Length Check: The program evaluates the length of the password, awarding points for passwords longer than 8, 12, 16, and 19 characters.

Common Password Check: The program reads a list of common passwords from a file (common.txt) and checks if the entered password is in that list. If it is, the score is set to 0.

Character Variety Points: Points are added based on the number of different character types found in the password.

Final Score and Feedback: The program calculates the total score and provides feedback on the strength of the password, categorizing it as "quite weak," "OKAY," "pretty good," or "strong."
