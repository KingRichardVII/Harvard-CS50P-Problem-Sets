#Richard Phan
#11/8/25

#Goal: This program converts a string with an emoticon into a string with an emoji

#function called convert, accept str as parameter
def convert(input_str):
    #chained replace statement
    modified_str = (input_str.replace(":)", "🙂").replace(":(", "🙁"))
    return modified_str

#All other text unchanged

#main function
def main():
    #prompt user for input
    hello_goodbye = input("Enter 'hello :)' or 'goodbye :(' ")
    #calls convert
    result = convert(hello_goodbye)
    #prints result (set return value to a variable. print the variable)
    print(result)
#call main
main()
