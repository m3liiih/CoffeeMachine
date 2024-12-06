def make_coffee():
    print("Starting to make coffee...\n"
          "Grinding coffee beans...\n"
          "Boiling water...\n"
          "Mixing the boiled water with ground coffee beans...\n"
          "Pouring the coffee into a cup...\n"
          "Adding some milk into the cup...\n"
          "Coffee is ready!")
make_coffee()

def ingredients_per(cups):
      water_ml = cups * 200
      milk_ml = cups * 50
      beans_g = cups * 20

      print(f"For {cups} cups of coffee you will need:")
      print(f"{water_ml} ml of water")
      print(f"{milk_ml} ml of milk")
      print(f"{beans_g} g of coffee beans")

cups = int(input("How many cups of coffee will you need: "))
ingredients_per(cups)