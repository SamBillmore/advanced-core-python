""" INSTRUCTIONS
----------------

The code below contains a minimal `ShoppingBasket` class, which keeps track of
a list of `Item`s.

* Run the code. You should see this error:
      TypeError: 'ShoppingBasket' object is not iterable

  This is because the code attempts to iterate through a `ShoppingBasket`
  instance, and the class does not have the required method.

* Update the `ShoppingBasket` class so that it is an iterable. Iterating through
  the shopping basket should behave the same as iterating through its list of
  Items.

--------------------------------------------------------------------------------

* Extension: If you finish the previous exercises then update the ShoppingBasket
  so that it iterates through item names, instead of the item objects.

  You will need to create a custom iterator class, and update the for loop,
  so that instead of printing item.name, it prints item_name:

  for item_name in my_basket:
      print(item_name)
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingBasket:
    def __init__(self):
        self.items = []

    def __iter__(self):
        # return iter(self.items)
        return ShoppingBasketIterator(self.items)

    def add_item(self, item):
        self.items.append(item)


class ShoppingBasketIterator:
    def __init__(self, items):
        self.items = items
        self.current_index = 0

    def __next__(self):
        if self.current_index >= len(self.items):
            raise StopIteration
        
        this_item = self.items[self.current_index]
        self.current_index += 1

        return this_item.name


my_basket = ShoppingBasket()
my_basket.add_item(Item("Butter", 1.00))
my_basket.add_item(Item("Toothpaste", 1.50))
my_basket.add_item(Item("Lightbulb", 4.00))
my_basket.add_item(Item("Tofu", 3.20))


# print("\nShopping basket contains:")
# for item in my_basket:
#     print(item.name)


print("\nShopping basket contains:")
for item_name in my_basket:
    print(item_name)
