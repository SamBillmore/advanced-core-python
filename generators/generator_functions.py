import time

from utils import format_big_int  # This function helps display large integers


"""
The function `fibonacci_numbers_list` below returns a list of the first `n`
Fibonacci numbers. This sequence starts with [1, 1] and then continues with
each new number being the sum of the previous two numbers:

So the third number is 1 + 1 = 2 => [1, 1, 2],
The fourth is 1 + 2 = 3 => [1, 1, 2, 3]
The fifth is 2 + 3 = 5 => [1, 1, 2, 3, 5] and so on.

You will implement the generator equivalent of this function,
`fibonacci_numbers_generator`, to do the same thing, but with a generator.

* Run this script, (`python3 <path>/generator_functions.py`) so you can see what the
  `test_fibonacci` function does, and make sure you understand the output.

* Uncomment the call to `test_fibonacci` at the bottom of this file, and update
  the `fibonacci_numbers_generator` function so that it generates the first
  `n` Fibonacci numbers.

* Run the script again, and notice the speed difference between the two
  functions (the sum of numbers produced should be the same).

* If you're feeling patient (this may take a while) try updating `COUNT` to
  `1_000_000` and run the script again.

  (on a modern machine, the generator function might take around 20s, whilst
  the list version could take well over 5 minutes).
"""


def fibonacci_numbers_list(n):
    """Return a list of the first n Fibonacci numbers"""
    previous = 0
    current = 1

    numbers = []
    for _ in range(n):
        numbers.append(current)
        previous, current = current, (previous + current)

    return numbers


def fibonacci_numbers_generator(n):
    """Generator function to produce the first n Fibonacci numbers"""
    previous = 0
    current = 1

    for _ in range(n):
        yield current
        previous, current = current, (previous + current)


# DON'T EDIT THE CODE BELOW THIS LINE (except to uncomment the function call)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def test_fibonacci(fibonacci_fun, count):
    print(f'\nUsing {fibonacci_fun.__name__}:')
    print('------------------------------------------------------------------')
    print(f"The first 10 Fibonacci numbers are: {list(fibonacci_fun(10))}")

    start_time = time.time()
    total = sum(fibonacci_fun(count))
    duration = time.time() - start_time

    print(f"The first {count} Fibonacci numbers sum to: {format_big_int(total)}")
    print(f"This calculation took {1000 * duration:.01f}ms")


COUNT = 100_000


test_fibonacci(fibonacci_numbers_list, COUNT)
test_fibonacci(fibonacci_numbers_generator, COUNT)
