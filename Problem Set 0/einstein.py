# Richard Phan
# 11/10/25

#Goal:
"""prompt user for mass as an integer (kg)
#output equivalent number of joules as integer
assume user will input an integer """


def equation(m):
    number = m * 300000000 **2 #**2 is the notation for squared
    return  number

def main():
    mass = int(input("m: "))
    result = equation(mass)
    print(result)
main()