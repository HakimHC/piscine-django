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


def is_state(s):
    return (s.lower() in list(states.keys()))

def is_capital(s):
    return (s.lower() in list(capital_cities.values()))

def get_dict_key_by_value(dct, s):
    res = list(dct.keys())[list(dct.values()).index(s)]
    return res

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc != 2):
        return 1

    for state in list(states):
        states[state.lower()] = states[state]
    caps = capital_cities.keys()
    for capital in list(capital_cities):
        capital_cities[capital.lower()] = capital_cities[capital]
        

    s = argv[1].split(",")
    s = [i.strip() for i in s]
    s.remove("")

    for i in s:
        if is_state(i):
            # print(f"{i} is a state")
            cap = capital_cities[states[i.lower()]]
            print(f"{cap} is the capital of {i}")
        elif is_capital(i):
            id = get_dict_key_by_value(capital_cities, i.lower())
            res = get_dict_key_by_value(states, id)
            print(f"{i} is the capital of {res}")
        else:
            print(f"{i} is neither a capital nor a state")


if __name__ == "__main__":
    main()
