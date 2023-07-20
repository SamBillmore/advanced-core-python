"""
The code below is very similar to the code in exercise 1. A ping is sent in a
loop, with the response logged.

This time, you'll write a new version of `add_delay`, which accepts an argument
to specify how long the delay should be. You can copy the `add_delay` decorator
from exercise 1 as a starting point.

1. Write your new `add_delay` decorator, which should expect one argument. This
   argument should specify the length of time (in seconds) to sleep before
   calling the wrapped function.

2. Uncomment the decorator line above the `send_ping` function. This should
   add a 1.5 second delay before each call. Run the script, and make sure that
   the pings are always > 1.5s apart.

3. Change the 1.5 to 3, and make sure that the ping spacing increases to > 3s
"""

import logging
import time
import functools

from utils import ping


# TODO: Write your new `add_delay` decorator here as a function
# def add_delay(delay_param):
#    def add_delay_parametrised(func):
#       @functools.wraps(func)
#       def wrapper(*args, **kwargs):
#          time.sleep(delay_param)
#          return func(*args, **kwargs)
#       return wrapper
#    return add_delay_parametrised


# TODO: Write your new `add_delay` decorator here as a class
# A better option for parametrised decorators
class add_delay:
    def __init__(self, delay):
        self.delay = delay

    def __call__(self, func):
      @functools.wraps(func)  # functools returns the correct thing here as it is decorating a function (closure)
      def wrapper(*args, **kwargs):
         time.sleep(self.delay)
         return func(*args, **kwargs)
      return wrapper


@add_delay(3)
def send_ping(url):
    logging.info("Sending ping to %s...", url)
    response = ping(url)
    logging.info("response code: %s\n", response)


while True:
    send_ping("http://adding_para.ms")
