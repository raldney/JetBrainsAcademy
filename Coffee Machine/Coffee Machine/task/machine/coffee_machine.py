### Coffe Machine

# Figure out how much of each ingredient the machine will need.
# Note that one cup of coffee made on this coffee machine contains
# 200 ml of water, 50 ml of milk, and 15 g of coffee beans
import math


class CoffeeMachine:
    COFFEE_RECIPE = {'1': {
        'water': 250,
        'coffee_beans': 16,
        'disposable_cups': 1,
        'price': 4
    }, '2': {
        'milk': 75,
        'water': 350,
        'coffee_beans': 20,
        'disposable_cups': 1,
        'price': 7
    }, '3': {
        'milk': 100,
        'water': 200,
        'coffee_beans': 12,
        'disposable_cups': 1,
        'price': 6
    }}

    def __init__(self):
        self._disposable_cups = 9
        self._money = 550
        self._water = 400
        self._milk = 540
        self._coffee_beans = 120

    def take_coffee(self, quantity):
        pass

    def do_withdraw(self):
        print('I gave you ${}'.format(self._money))
        self._money = 0

    def fill_machine(self, ingredients):
        self._disposable_cups += ingredients['disposable_cups']
        self._water += ingredients['water']
        self._milk += ingredients['milk']
        self._coffee_beans += ingredients['coffee_beans']

    def prepare_coffee(self, coffee_type):
        if coffee_type not in self.COFFEE_RECIPE:
            print('Invalid Option!')
            return False

        for ingredient in self.COFFEE_RECIPE[coffee_type]:
            if ingredient == 'price':
                break
            if not self.verify_ingredients(ingredient, coffee_type):
                return None

        print('I have enough resources, making you a coffee!')

        for ingredient in self.COFFEE_RECIPE[coffee_type]:
            if ingredient != 'price':
                ingredient_quantity = self.__getattribute__('_' + ingredient) - self.COFFEE_RECIPE[coffee_type][
                    ingredient]
                self.__setattr__('_' + ingredient, ingredient_quantity)

        self._money += self.COFFEE_RECIPE[coffee_type]['price']
        return True

    def verify_ingredients(self, ingredient_type, coffee_type):
        print(ingredient_type in self.COFFEE_RECIPE[coffee_type], ingredient_type)
        if ingredient_type in self.COFFEE_RECIPE[coffee_type]:
            if self.__getattribute__('_' + ingredient_type) / self.COFFEE_RECIPE[coffee_type][ingredient_type] < 1:
                return False
        return True

    def print_supplies(self):
        print("The coffee machine has:\n"
              "{} of water\n"
              "{} of milk\n"
              "{} of coffee beans\n"
              "{} of disposable cups\n"
              "${} of money\n"
              .format(self._water, self._milk, self._coffee_beans, self._disposable_cups, self._money))


coffee_machine = CoffeeMachine()

while True:
    option = input('Write action (buy, fill, take, remaining, exit):\n')
    if option == 'fill':
        qtd_water = int(input("Write how many ml of water do you want to add:"))
        qtd_milk = int(input("Write how many ml of milk do you want to add:"))
        qtd_coffee = int(input("Write how many grams of coffee beans do you want to add:"))
        qtd_cups = int(input("Write how many disposable cups do you want to add:"))
        new_ingredients = {'water': qtd_water, 'milk': qtd_milk, 'coffee_beans': qtd_coffee, 'disposable_cups': qtd_cups}
        coffee_machine.fill_machine(new_ingredients)
    elif option == 'take':
        coffee_machine.do_withdraw()
        pass
    elif option == 'buy':
        coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back:')
        if coffee_type != '4':
            coffee_machine.prepare_coffee(coffee_type)
    elif option == 'exit':
        break
    elif option == 'remaining':
        coffee_machine.print_supplies()
    else:
        print('Invalid Option!')