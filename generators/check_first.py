"""
The function `check_first` should receive a generator, and return its first
item, along with a generator that produces the original set of values.

* Run this script. You should see that `check_first` correctly returns the first
  item, but that the generator it returns no longer contains this item.

* Update this code so that the generator returned by check_first includes the
  exact same set of items as the input generator. You might need to write an
  additional function

  The output you see should be:

  The first square number is 1
  The first twelve square numbers are:
  1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144,
"""


def check_first(generator):
    first_item = next(generator)
    return first_item, recreate_generator(first_item, generator)


def recreate_generator(first_item, generator):
    yield first_item
    yield from generator


# DON'T EDIT THE CODE BELOW THIS LINE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

square_numbers = (x ** 2 for x in range(1, 13))

first_square, square_numbers = check_first(square_numbers)

print("\nThe first square number is", first_square)
print("The first twelve square numbers are:")
for square in square_numbers:
    print(square, end=', ')
print()
