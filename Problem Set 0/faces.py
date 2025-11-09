#Richard Phan
#11/8/25

#Goal: This program converts a string with an emoticon into a string with an emoji

#function called convert, accept str as parameter
def convert(input_str):
    #RETURNS same input with emoticon converted to 🙂 or 🙁
    return input_str.replace(":),🙂")
#All other text unchanged

#main function
def main():
    #prompt user for input
    hello_goodbye = input("Enter 'hello :)' or 'goodbye :(' ")
    #calls convert
    convert(hello_goodbye)
    #prints result (set return value to a variable. print the variable)
    result = convert(hello_goodbye)
    print(result)
#call main
main()
