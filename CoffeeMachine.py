def make_coffee():
    print("Starting to make coffee...\n"
          "Grinding coffee beans...\n"
          "Boiling water...\n"
          "Coffee is ready to mix!")
make_coffee()
print()

def ingredients_for(cups):
      water_ml = cups * 200
      milk_ml = cups * 50
      beans_g = cups * 10

      print(f"For {cups} cups of coffee you need:")
      print(f"{water_ml} ml of water")
      print(f"{milk_ml} ml of milk")
      print(f"{beans_g} g of coffee beans")


def resources(water_available, milk_available, beans_available, cups_needed):
      water_limited_cups = water_available // 200
      milk_limited_cups = milk_available // 50
      bean_limited_cups = beans_available // 10

      max_cups_of_coffee = min(water_limited_cups, milk_limited_cups, bean_limited_cups)

      if max_cups_of_coffee >= cups_needed:
            print("I can make that much coffee for your meeting.")
      else:
            print(f"I can't make that much but I can make {max_cups_of_coffee} cups.")

def machine_stock(water, milk, beans, cups, money):
      print("The coffee machine has:")
      print(f"{water} ml of water")
      print(f"{milk} ml of milk")
      print(f"{beans} g of coffee beans")
      print(f"{cups} coffee cups")
      print(f"${money} of money")


def buy_coffee(water, milk, beans, cups, money):
      print("What type of coffee would you like to buy?\n1 - espresso, 2 - latte, 3 - cappuccino, 0 - back")
      coffee_type = input("-- ")

      if coffee_type == 0:
            return water, milk, beans, cups, money

      if coffee_type == "1":
            water_needed = 200
            milk_needed = 0
            beans_needed = 10
            price = 3
      elif coffee_type == "2":
            water_needed = 200
            milk_needed = 25
            beans_needed = 10
            price = 5
      elif coffee_type == "3":
            water_needed = 200
            milk_needed = 50
            beans_needed = 10
            price = 7.5
      else:
            print("Please select a valid option.")
            return water, milk, beans, cups, money

      if water >= water_needed and milk >= milk_needed and beans >= beans_needed and cups >= 1:
          print("Making your coffee... Enjoy!")
          return water - water_needed, milk - milk_needed, beans - beans_needed, cups - 1, money + price
      else:
            print("Sorry, not enough resources.")


def add_resources(water, milk, beans, cups):
      water = water + int(input("How many ml of water do you want to add: "))
      milk = milk + int(input("How many ml of milk do you want to add: "))
      beans = beans + int(input("How many g of coffee beans do you want to add: "))
      cups = cups + int(input("How many coffee cups do you want to add: "))
      return water, milk, beans, cups

def collect_money(money):
      if input("Please use the key to collect money: ") == "key" :
            print(f"Collected ${money}")
            money = 0
      else:
            print("Wrong key.")
      return money
