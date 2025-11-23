# Richard Phan
# 11/16/25

#GOAL: In a file called bank.py, implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    #prompt user for greeting. append .strip() and append .lower()
    greeting = input("Greeting: " ).strip().lower()

    #if starts with hello print $0
    if greeting.startswith("hello"): #.startswith = "Does the string being with ____"
        print("$0")
    #elif starts with "h' print $0
    elif greeting.startswith("h"):
        print("$20")
    # else output $100
    else:
        print("$100")
main()