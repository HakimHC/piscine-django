def main():
    with open("numbers.txt", "r") as f:
        s = f.read()
        s = s.replace("\n", "")
        for i in s.split(","):
            print(i)

if __name__ == "__main__":
    main()
