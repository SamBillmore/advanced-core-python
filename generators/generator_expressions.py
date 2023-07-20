import tracemalloc

from utils import display_malloc_snapshot  # Neat display of memory trace

"""
The code below uses a list comprehension to generate all possible three letter
combinations in a list called `three_letter_combos_list`.

* Update the definition of `three_letter_combos_generator` to do the same thing
but with a generator expression.

* Run this script. The `tracemalloc` package is used to trace which lines of
code allocate memory, and how much is allocated. Compare the amount of memory
allocated for the list comprehension and the generator expression.

* The final output displays the first few results from the generator, and then
the number of items in the list comprehension and the generator expression. If
these numbers are different, why do you think that is?

Answer: because call `next` on generator before printing the length.
Aka, already used part of generator.
"""

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


tracemalloc.start()  # Start profiling memory use


three_letter_combos_list = [
    letter_1 + letter_2 + letter_3
    for letter_1 in LETTERS
    for letter_2 in LETTERS
    for letter_3 in LETTERS]


# TODO: Update this definition
three_letter_combos_generator = (
    letter_1 + letter_2 + letter_3
    for letter_1 in LETTERS
    for letter_2 in LETTERS
    for letter_3 in LETTERS)


# DON'T EDIT THE CODE BELOW THIS LINE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This code looks at current memory usage, and displays the results
memory_snapshot = tracemalloc.take_snapshot()
display_malloc_snapshot(memory_snapshot)
tracemalloc.stop()  # Stop profiling memory use


print("---------------------------------")
print("The first three letter combos are:")
print(next(three_letter_combos_generator))
print(next(three_letter_combos_generator))
print(next(three_letter_combos_generator))
print("---------------------------------")
print()

print("Generator expression contains", len(list(three_letter_combos_generator)), "items")
print("List comprehension contains", len(three_letter_combos_list), "items")
