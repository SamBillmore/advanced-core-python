# DO NOT CHANGE ANY OF THE CODE HERE!
# These constants and function are used by the code later on

VOWELS = set('AEIOU')
CONSONANTS = set('BCDFGHJKLMNPQRSTVWXYZ')

def vowel_requested():
    """Returns True if the user requests a vowel, and False for a consonant"""
    while True:
        response = input('\nWould you like a vowel (v) or a consonant (c)? ')
        if response.lower() == 'v':
            return True
        elif response.lower() == 'c':
            return False
        else:
            print("Please enter the letter 'c' or 'v' and then press Enter")


""" INSTRUCTIONS
----------------

The British game show Countdown has a round where contestants have to make the
longest word they can with 9 letters.
At the start, a contestant picks random letters one at a time, and can choose
whether to pick a consonant or vowel. Once a letter has been picked, it can
not be picked for a second time.

The function `select_countdown_letters` below implements this by popping items
from a `set` of vowels, and a `set` of consonants. For each letter it uses the
function `vowel_requested` to ask the user if they would like a vowel (True)
or consonant (False).

* Run the file (`python3 iterators.py`) to see how the function works.
  Once you have picked 9 letters, the code should raise an AssertionError,
  because of a test that the sets of `VOWELS` and `CONSONANTS` have not been
  changed. At the moment, they are being changed, because the function
  `select_countdown_letters` uses `pop` to remove items.

* Use iterators to update this function so that it no longer modifies the sets.
  It should still only return each vowel and consonant at most once (no repeated
  letters).

  To do this you should:
    1. Create new iterators for the sets `VOWELS` and `CONSONANTS`.
    2. Use these iterators to return values instead of popping them from a set.

* Run the code again, and check that the `assert` statements do not raise any
  errors.
"""


def select_countdown_letters():
    letters = ''
    iter_vowels = iter(VOWELS)
    iter_consonants = iter(CONSONANTS)

    for _ in range(9):
        if vowel_requested():
            try:
                next_letter = next(iter_vowels)
            except StopIteration:
                next_letter = next(iter_consonants)
        else:
            next_letter = next(iter_consonants)

        letters += next_letter
        print('Your letters are:', letters)

    return letters


print('\n', 'Your set of letters is:', select_countdown_letters(), '\n')



# Make sure that the original letter sets have not been changed
# DO NOT CHANGE THESE LINES!
assert VOWELS == set('AEIOU'), 'the constant VOWELS has been modified'
assert CONSONANTS == set('BCDFGHJKLMNPQRSTVWXYZ'), 'the constant CONSONANTS has been modified'
