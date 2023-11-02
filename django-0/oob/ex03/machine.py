from beverages import HotBeverage, Chocolate
import random

class CoffeeMachine:
    def __init__(self) -> None:
        self.count = 0
        pass

    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            self.name = "empty cup"
            self.price = 0.90
            self.desc = "An empty cup?! Gimme my money back"

    class BrokenMachineException(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__("This coffee machine has to be repaired")

    def repair(self):
        self.count = 0
    
    def serve(self, cup):
        # if not isinstance(cup, HotBeverage):
        #     raise Exception("Not a hot beverage instance")
        if self.count >= 10:
            raise self.BrokenMachineException()
        arr = [cup, self.EmptyCup()]
        self.count += 1
        return arr[random.randint(0, 1)]

    
    def test(self):
        raise self.BrokenMachineException()


def main():
    cm = CoffeeMachine()
    for i in range(10):
        print(type(cm.serve(HotBeverage())).__name__)
    
    try:
        cm.serve(HotBeverage())
    except CoffeeMachine.BrokenMachineException as e:
        print(e)

    cm.repair()
    print(type(cm.serve(HotBeverage())).__name__)
    


if __name__ == "__main__":
    main()