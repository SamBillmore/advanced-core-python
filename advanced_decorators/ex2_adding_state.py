"""
The code below is very similar to the code in exercise 1. A ping is sent in a
loop, with the response logged.

In exercise 1, you added a decorator which added a 1 second delay as a way of
limiting the rate of calls to `send_ping`. Because the ping itself takes some
time, this meant the pings weren't 1s apart, but somewhere between 1.1 and 1.5s
apart.

1. Write a new `rate_limit` decorator, which will ensure that its wrapped
   function cannot be called until 1 second after its previous call (if one has
   already happened).

   This decorator needs to keep track of the exact time when its wrapped
   function was last called. It can do this using `time.time()` like the
   `send_ping` function does.

   Then, if less than a second has passed, `rate_limit` should use `time.sleep`
   to wait long enough that a second will have passed before its wrapped
   function is called again.

2. Use the `rate_limit` decorator to wrap the `send_ping` function, and run the
   script. You should see exactly 1s between each call to ping.

"""


import logging
import time
import functools

from utils import ping


# TODO: write the rate_limit decorator here
class _rate_limit():
   def __init__(self, func):
      self.func = func
      self.last_run = 0

   def __call__(self, *args, **kwargs):
      current_time = time.time()
      time_since_last_run = current_time - self.last_run
      if time_since_last_run < 1:
         sleep_time = 1 - time_since_last_run
         time.sleep(sleep_time)
      self.last_run = time.time()
      return self.func(*args, **kwargs)
   
# Used to make sure functools is returning the correct things
def rate_limit(func):
    r_l = _rate_limit(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return r_l(*args, **kwargs)

    return wrapper


@rate_limit
def send_ping(url):
    logging.info("Sending ping to %s...", url)
    start = time.time()
    response = ping(url)
    logging.debug("Ping took %.02fs to respond", time.time() - start)
    logging.info("response code: %s\n", response)


while True:
    send_ping("www.exercise2.com")
