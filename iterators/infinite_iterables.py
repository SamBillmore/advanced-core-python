import time


""" INSTRUCTIONS
----------------

* If you try to run this program at the moment, it will break because
  InfiniteCycle is not an iterable.

* Without changing the code in the for loop, update the InfiniteCycle class so
  that it is an iterable which cycles through all of its items without ever
  terminating. For example:

  for item in InfiniteCycle([1, 2, 3]):
      print(item)

  should print out the numbers 1, 2, 3, 1, 2, 3, 1, 2, 3, ... etc.
"""

class InfiniteCycle:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return InfiniteCycleIterator(self.items)
    

class InfiniteCycleIterator:
    def __init__(self, items):
        self.current_index = 0
        self.items = items

    def __next__(self):
        return_val = self.items[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.items)
        return return_val


# DO NOT EDIT ANY CODE BELOW HERE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("This will go on for")
for item in InfiniteCycle(["ever", "and"]):
    time.sleep(1)  # Wait 1 second
    print(item)
