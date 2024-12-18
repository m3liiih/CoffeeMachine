def make_coffee():
    print("Starting to make coffee...\n"
          "Grinding coffee beans...\n"
          "Boiling water...\n"
          "Coffee is ready to mix!")
make_coffee()
print()

water = 4000
milk = 1200
beans = 250
cups = 30
money = 0


def ingredients_for(water, milk, beans, cups, money, cups2make):
      water_ml = cups2make * 200
      milk_ml = cups2make * 50
      beans_g = cups2make * 10

      print(f"For {cups} cups of coffee you need:")
      print(f"{water_ml} ml of water")
      print(f"at most {milk_ml} ml of milk")
      print(f"{beans_g} g of coffee beans")

      machine_stock(water, milk, beans, cups, money)


def max_cups(water_available, milk_available, beans_available, cups_needed):
      water_limited_cups = water_available // 200
      milk_limited_cups = milk_available // 50
      bean_limited_cups = beans_available // 10

      max_cups_of_coffee = min(water_limited_cups, milk_limited_cups, bean_limited_cups)

      if max_cups_of_coffee >= cups_needed:
            print("I can make that much coffee for your meeting.")
      else:
            print(f"I can't make that much but I can make {max_cups_of_coffee} cups.")
      print()
      return max_cups_of_coffee


def machine_stock(water, milk, beans, cups, money):
      print("The coffee machine currently has:")
      print(f"{water} ml of water")
      print(f"{milk} ml of milk")
      print(f"{beans} g of coffee beans")
      print(f"{cups} coffee cups")
      print(f"${money} of money")
      print()


def buy_coffee(water, milk, beans, cups, money, count):
      print("What type of coffee would you like to buy?\n1 - espresso, 2 - latte, 3 - cappuccino, 0 - back")
      coffee_type = input("-- ")

      if coffee_type == 0:
            return water, milk, beans, cups, money

      if coffee_type == "1":
            water_needed = 200 * count
            milk_needed = 0 * count
            beans_needed = 10 * count
            price = 3 * count
      elif coffee_type == "2":
            water_needed = 200 * count
            milk_needed = 25 * count
            beans_needed = 10 * count
            price = 5 * count
      elif coffee_type == "3":
            water_needed = 200 * count
            milk_needed = 50 * count
            beans_needed = 10 * count
            price = 7.5 * count
      else:
            print("Please select a valid option.\n")
            return water, milk, beans, cups, money

      if water >= water_needed and milk >= milk_needed and beans >= beans_needed and cups >= 1:
          print("Making your coffee... Enjoy!\n")
          return water - water_needed, milk - milk_needed, beans - beans_needed, cups - 1, money + price
      else:
            print("Sorry, not enough resources.")
      print()


def add_resources(water, milk, beans, cups):
      water += + int(input("How many ml of water do you want to add: "))
      milk += int(input("How many ml of milk do you want to add: "))
      beans += int(input("How many g of coffee beans do you want to add: "))
      cups += int(input("How many coffee cups do you want to add: "))
      machine_stock(water, milk, beans, cups, money)
      return water, milk, beans, cups

def collect_money(money):
      if input("Please use the key to collect money: ") == "key" :
            print(f"Collected ${money}\n")
            money = 0
      else:
            print("Wrong key.\n")
      return money


while True:
      action = input("Select an action (buy, menu, maintenance): ")

      if action == "buy":
            mode = int(input("Select mode 1 - single, 2 - multiple, 0 - back: "))
            if mode == 1:
                  water, milk, beans, cups, money = buy_coffee(water, milk, beans, cups, money, 1)
            elif mode == 2:
                  count = int(input("How many cups would you like? "))
                  max = max_cups(water, milk, beans, count)
                  if count <= max:
                        water, milk, beans, cups, money = buy_coffee(water, milk, beans, cups, money, count)
                        print(f"Here's your {count} cups of coffee, enjoy your meeting.\n")
            elif mode == 0:
                  print()
            else:
                  print("Invalid mode selection")
                  print()



      elif action == "menu":
            print("Espresso $3\nLatte $5\nCappuccino $7.5\n")


      elif action == "maintenance":
            m_mode = int(input("Select mode 1 - stock, 2 - refill, 3 - collect, 0 - back: "))
            if m_mode == 1:
                  machine_stock(water, milk, beans, cups, money)
            elif m_mode == 2:
                  water, milk, beans, cups = add_resources(water, milk, beans, cups)
            elif m_mode == 3:
                  money = collect_money(money)
            elif m_mode == 0:
                  print()
            else:
                  print("Invalid maintenance mode")
      else:
            print("Invalid action")