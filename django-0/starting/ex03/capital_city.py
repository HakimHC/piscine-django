import sys


states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}

capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}


def main():
    argv = sys.argv
    argc = len(argv)

    if (argc != 2):
        return 1

    if argv[1] not in states:
        print("Unknown state")
        return 1

    print(capital_cities[states[argv[1]]])

if __name__ == "__main__":
    main()

