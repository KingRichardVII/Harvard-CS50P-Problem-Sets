# Richard Phan
# 11/15/25

#GOAL: prompt user for input. Outputs yes if user inputs 42 or forty-two or forty two. otherwise output no.

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    if not (answer == "42" or answer == "forty-two" or answer == "forty two" or answer == "Forty Two"):
        print("No")
    else:
        great_question(answer)


def great_question(machine_answer):
        print("Yes")
main()