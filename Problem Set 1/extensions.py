#Richard Phan
#11/22/25

#Goal: In a file called extensions.py, implement a program that prompts the user for the name of a file and then
# outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
""".gif
.jpg
.jpeg
.png
.pdf
.txt
.zip """

def main():
    file = input("File name: ")

    if file.endswith(".gif"): #.endswith = "Does the string end with ____"
        print("image/gif")
    elif file.endswith(".jpg"):
        print("image/jpeg")
    elif file.endswith(".jpeg"):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.strip().lower().endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()