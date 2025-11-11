# Richard Phan
# 11/10/25

#Goal: complete the following functions:
#dollars to float - function which changes the data type from str to float
#percent to float - function which changes 15% to a float 15.00, then 0.15

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #replace() gets rid of $,  float changes data type of input
    return float(d.replace("$", ""))

def percent_to_float(p):
    return float(p.replace("%", "")) / 100 #divide by 100- reasoning: user inputs 15% not actually .15


main()