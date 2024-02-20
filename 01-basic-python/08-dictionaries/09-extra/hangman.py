import random

def lees_woordenlijst(input):
    with open(input) as word_list:
        result = [word.strip() for word in word_list.realine()]
    return result

def check_list(woord, lijst):
    complete = True
    print_solution = ""
    for w in woord:
        print
        if w in lijst:
            print_solution += w

        else:
            complete = False
    print(f"Resultaat = {print_solution}")
    return complete

def main():
    levens = 6
    input_list = []
    woordenlijst = lees_woordenlijst("gangman.txt")
    random.choice(woordenlijst)

    choice = input("Kies een letter: ")
    if choice.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("Idioot")
    else:
        input_list.append(choice.upper())

main()