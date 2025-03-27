class CoffeeMachine:
    def __init__(self):
        self.water = 2400
        self.milk = 800
        self.beans = 250
        self.cups = 20
        self.money = 0

    def make_coffee(self):
        print("Starting to make coffee...\n"
              "Grinding coffee beans...\n"
              "Boiling water...\n"
              "Coffee is ready to mix!\n")

    def buy_coffee(self, coffee, count):
        water_needed = coffee.water * count
        milk_needed = coffee.milk * count
        beans_needed = coffee.beans * count
        price = coffee.price * count

        if self.water >= water_needed and self.milk >= milk_needed and self.beans >= beans_needed and self.cups >= count:
            if count == 1:
                print("Making your coffee... Enjoy!")
            if count > 1:
                print(f"\nHere's your {count} cups of coffee, enjoy!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.beans -= beans_needed
            self.cups -= count
            self.money += price
        else:
            print("Sorry, not enough resources.")
        print()

    def max_cups(self, cups_needed):
        water_limited_cups = self.water // 200
        milk_limited_cups = self.milk // 50
        bean_limited_cups = self.beans // 10
        max_cups_of_coffee = min(water_limited_cups, milk_limited_cups, bean_limited_cups)
        if max_cups_of_coffee >= cups_needed:
            print("I can make that much coffee for you.")
        else:
            print(f"I can't make that much but I can make {max_cups_of_coffee} cups.")
        print()
        return max_cups_of_coffee

    def show_stock(self):
        print("The coffee machine currently has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.beans} g of coffee beans")
        print(f"{self.cups} coffee cups")
        print(f"${self.money} of money\n")

    def add_resources(self):
        self.water += int(input("How many ml of water do you want to add (max:4000): "))
        self.milk += int(input("How many ml of milk do you want to add (max:1200): "))
        self.beans += int(input("How many g of coffee beans do you want to add (max:300): "))
        self.cups += int(input("How many coffee cups do you want to add (max:24): "))
        water_max, milk_max, beans_max, cups_max = 4000, 1200, 300, 24
        self.water = min(self.water, water_max)
        self.milk = min(self.milk, milk_max)
        self.beans = min(self.beans, beans_max)
        self.cups = min(self.cups, cups_max)
        print()
        self.show_stock()

    def collect_money(self):
        if input("Please use the key to collect money: ") == "key":
            print(f"Collected ${self.money}\n")
            self.money = 0
        else:
            print("Wrong key.\n")

class Coffee:
    def __init__(self, name, water, milk, beans, price):
        self.name = name
        self.water = water
        self.milk = milk
        self.beans = beans
        self.price = price

    def menu(self):
        return f"{self.name} ${self.price}"

espresso = Coffee("Espresso", 200, 0, 10, 3)
latte = Coffee("Latte", 200, 25, 10, 5)
cappuccino = Coffee("Cappuccino", 200, 50, 10, 7.5)

cf_machine = CoffeeMachine()
cf_machine.make_coffee()

while True:
    action = input("Select an action (buy, menu, maintenance): ")

    if action == "buy":
        mode = int(input("Select mode 1 - single, 2 - multiple, 0 - back: "))
        if mode == 1:
            print("What type of coffee would you like to buy?\n1 - espresso, 2 - latte, 3 - cappuccino, 0 - back")
            coffee_type = input("-- ")
            if coffee_type == "1":
                cf_machine.buy_coffee(espresso, 1)
            elif coffee_type == "2":
                cf_machine.buy_coffee(latte, 1)
            elif coffee_type == "3":
                cf_machine.buy_coffee(cappuccino, 1)
            elif coffee_type == "0":
                print()
            else:
                print("Please select a valid option.\n")
        elif mode == 2:
            count = int(input("How many cups would you like? "))
            max_cups = cf_machine.max_cups(count)
            if count <= max_cups:
                print("What type of coffee would you like to buy?\n1 - espresso, 2 - latte, 3 - cappuccino, 0 - back")
                coffee_type = input("-- ")
                if coffee_type == "1":
                    cf_machine.buy_coffee(espresso, count)
                elif coffee_type == "2":
                    cf_machine.buy_coffee(latte, count)
                elif coffee_type == "3":
                    cf_machine.buy_coffee(cappuccino, count)
                elif coffee_type == "0":
                    print()
                else:
                    print("Please select a valid option.\n")

        elif mode == 0:
            print()
        else:
            print("Invalid mode selection\n")

    elif action == "menu":
        print(espresso.menu())
        print(latte.menu())
        print(cappuccino.menu())
        print()

    elif action == ("maintenance"):
        m_mode = input("Select mode 1 - stock, 2 - refill, 3 - collect, 0 - back: ")
        if m_mode == "1":
            cf_machine.show_stock()
        elif m_mode == "2":
            cf_machine.add_resources()
        elif m_mode == "3":
            cf_machine.collect_money()
        elif m_mode == "0":
            print()
        else:
            print("Invalid maintenance mode\n")
    else:
        print("Invalid action\n")