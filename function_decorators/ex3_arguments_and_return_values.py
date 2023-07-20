"""
The `product` function takes a collection of items, and calculates their product
(multiplies all items together using `*`).

1. Run this script - you should see that at least one of the test cases for
   product raises an error.

2. Decorate `product` with the `catch_errors` decorator.
   (you can either import this directly from ex2_decorator_functions, or copy
   catch_errors from that file into this one)

3. Update the definition of the `catch_errors` decorator so the functions it
   decorates can:
   * receive positional and keyword arguments (*args and **kwargs)
   * return a value

4. Run this script again, and ensure that the test cases are all run, with
   error messages printed for the 3rd and 5th examples
"""

from ex2_decorator_functions import catch_errors

@catch_errors
def product(collection, inverse=False):
    result = 1
    for value in collection:
        result = result * value

    if inverse:
        return 1 / result
    else:
        return result


if __name__ == "__main__":
    print(f"\nTEST CASES (for the function: {product.__name__})\n----------")
    test_cases = [
        ([4, 5], False),
        ([0, 1, 2, 3], False),
        (['a', 'b', 'c'], False),
        (['a', 3, 2], False),
        ([0, 1, 2, 3], True),
        ([2, 2, 2], True),
    ]

    # Run the test cases one at a time and print out results
    for index, (collection, inverse) in enumerate(test_cases, start=1):
        print(f"Test {index}.", end=' ')
        if inverse:
            print("inverse", end=' ')
        print(f"product of {collection}:", end=' ')
        result = product(collection, inverse=inverse)
        if result is not None:
            print(result)
