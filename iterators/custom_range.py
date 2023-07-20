"""INSTRUCTIONS
---------------

The built-in `range` function in Python isn't actually a function; it's an
iterable class that lets you iterate over integers. For example:

for i in range(3, 7)

will iterate over the values 3, 4, 5, 6, assigning each value to the variable i.

The `CustomRange` class below will replicate the behaviour of `range`, taking
in `start` and `end` values for a sequence of numbers.

It will also accept a `transform` argument. This should be a function that
takes in a value, and returns the next value in a sequence. If you wanted a
sequence that increased by 5 each time, `transform` would be: `lambda x: x + 5`

For example:

CustomRange(10, 30, transform=lambda x: x + 5) should generate the sequence 10, 15, 20, 25
CustomRange(2, 20, transform=lambda x: 2*x - 1) should generate the sequence 2, 3, 5, 9, 17


* Update the methods `__iter__` and `__next__` on `CustomRange` so that the
  iterations at the bottom of this file work correctly

* You will have to add a new attribute to CustomRange to keep track of the
  current iteration position, and update this in the `__iter__` and `__next__`
  methods.

* Run the code and make sure that the sequences printed look correct.
"""


class CustomRange:
    def __init__(self, start, end, transform=lambda x: x + 1):
        self.start = start
        self.end = end
        self.transform = transform

    def __iter__(self):
        self.current_value = self.start
        return self

    def __next__(self):
        if self.current_value >= self.end:
            raise StopIteration
        
        return_item = self.current_value
        self.current_value = self.transform(self.current_value)
    
        return return_item




# This should print odd numbers between 40 and 50: 41, 43, 45 etc.
print('\nOdd numbers from 40 to 50')
for i in CustomRange(41, 50, lambda x: x + 2):
    print(i)

# This should print all the powers of 2 less than 100: 1, 2, 4, 8, etc.
print('\nPowers of 2 up to 100')
for i in CustomRange(1, 100, lambda x: x * 2):
    print(i)

# Each iteration should return the square of the previous number:
# 2, 4, 16, 256 etc. up to 10 billion.
print('\nRepeated squares up to 10 billion')
for i in CustomRange(2, 10_000_000_000, lambda x: x ** 2):
    print(i)
