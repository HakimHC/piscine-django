class Intern:
    def __init__(self, name = "My name? I'm nobody, an intern, I have no name") -> None:
        self.name = name
    
    def __str__(self) -> str:
        return self.name

    def work(self):
        raise Exception("I'm just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()

    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."


def main():
    intern = Intern()
    mark = Intern("Mark")

    coffee = mark.make_coffee()
    print(coffee)
    try:
        intern.work()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()