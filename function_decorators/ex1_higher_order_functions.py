"""
* Update the definition of the chain function below, so it returns a new
  'compound' function, which first applies `function_1` and then `function_2.
  You can assume that function_1 and function_2 each take a single positional
  argument.

  >>> new_function = chain(function_1, function_2)
  >>> result = new_function([1, 2, 3])

  should be equivalent to calling:

  >>> result = function_2(function_1([1, 2, 3]))


  Examples:
  >>> double_sum = chain(sum, lambda x: x * 2)
  >>> double_sum([1, 2, 3])
  12
  >>> to_percent = chain(lambda x: x * 100, round)
  >>> to_percent(0.32652)
  33

* The chain function is already used further down in the file to create a
  CamelCaseNameGenerator function. Run this script to check `chain` is working
  as intended.
"""

# Each of these functions expects one string argument, and returns a string
from utils import titlecase, remove_spaces, lowercase_first_letter


def chain(function_1, function_2):
    def wrapper(value):
        return function_2(function_1(value))
    return wrapper


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# <<<<< DO NOT EDIT THE CODE BELOW HERE >>>>>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

name = "engelbert humpbackdinck"

# Create a new function using chain
upper_camelcase = chain(titlecase, remove_spaces)

print("\nOriginal Name:", name)
print("Upper Camelcase Name:", upper_camelcase(name), "\n")


"""
PART 2 - Make chain accept a generic number of functions
--------------------------------------------------------

* Update the condition on the line below to `if True`.
* Update the `chain` function above, so that instead of taking 2 functions as
  arguments, it takes an arbitrary number of functions using `*args`.
"""

def chain(*functions):
    def wrapper(value):
        for function in functions:
            value = function(value)
        return value
    return wrapper

if True:  # TODO: Change this condition to True to attempt part 2
    lower_camelcase = chain(titlecase, remove_spaces, lowercase_first_letter)

    print("Lower Camelcase Name:", lower_camelcase(name))


"""
PART 3 - Optional
-----------------

* Update the chain function so that the first function can receive arbitrary
  arguments (using *args, and **kwargs). This shouldn't change any of your
  results, but would allow the following example to work:

  >>> first_three = chain(sorted, lambda x: x[:3])
  >>> first_three([1, 5, 3, 4, 2, 6], reverse=True)
  [6, 5, 4]

  (reverse is an optional keyword argument to the built-in sorted function)
"""

def chain(function_1, function_2):
    def wrapper(*args, **kwargs):
        return function_2(function_1(*args, **kwargs))
    return wrapper





# perform checks on the results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

expected_upper = "EngelbertHumpbackdinck"
if upper_camelcase(name) != expected_upper:
    print(f"ERROR: upper_camelcase not working - expected value was {expected_upper}")


if 'lower_camelcase' in locals():
    expected_lower = "engelbertHumpbackdinck"
    if lower_camelcase(name) != expected_lower:
        print(f"ERROR: lower_camelcase not working - expected value was {expected_lower}")
