class HotBeverage:
    def __init__(self) -> None:
        self.price = 0.30
        self.name = "hot beverage"
        self.desc = "Just some hot water in a cup."

    def description(self):
        return self.desc
    
    def __str__(self) -> str:
        s = f"""name: {self.name}
            price: {self.price}
            description: {self.description()}"""

        return "\n".join(i.lstrip() for i in s.split("\n"))
    
class Coffee(HotBeverage):
    def __init__(self) -> None:
        self.name = "coffee"
        self.price = 0.40
        self.desc = "A coffee to stay awake"

class Tea(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.name = "tea"

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self.name = "chocolate"
        self.price = 0.50
        self.desc = "Chocolate, sweet chocolate.."
    
class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self.name = "cappuccino"
        self.price = 0.45
        self.desc = "Un po' di Italia nella sua tazza!"
    
# def main():
#     bev = HotBeverage()
#     coffee = Coffee()
#     tea = Tea()
#     chocolate = Chocolate()
#     cappuccino = Cappuccino()

#     print(bev, end="\n=====\n")
#     print(coffee, end="\n=====\n")
#     print(tea, end="\n=====\n")
#     print(chocolate, end="\n=====\n")
#     print(cappuccino, end="\n=====\n")

# if __name__ == "__main__":
#     main()