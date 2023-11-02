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


def get_dict_key_by_value(dct, s):
    res = list(dct.keys())[list(dct.values()).index(s)]
    return res

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc != 2):
        return 1

    if argv[1] not in list(capital_cities.values()):
        print("Unknown capital city")
        return 1

    id = get_dict_key_by_value(capital_cities, argv[1])
    print(get_dict_key_by_value(states, id))

if __name__ == "__main__":
    main()

