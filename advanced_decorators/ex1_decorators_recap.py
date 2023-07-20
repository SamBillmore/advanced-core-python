"""
The code below repeatedly sends a ping to the same url and logs the response.
Each call to `ping(url)` also logs a debug message to show the amount of time
between subsequent calls.

You will write a decorator which adds a 1 second delay as a way of rate
limiting the calls to `send_ping` (so calls will be at least 1 second apart).

1. Run the script. You should see that the time between pings varies, but is
   always less than 0.6s.

2. Write a function decorator called `add_delay`, which adds a 1 second delay
   before calling the wrapped function. You can do this using `time.sleep(1)`.

3. Use `add_delay` to decorate `send_ping`, and run the script again. You should
   see that all intervals are now > 1s.
"""

import logging
import time
import functools

from utils import ping


# TODO: Write the `add_delay` decorator here
def add_delay(func):
    @functools.wrap(func)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper


@add_delay
def send_ping(url):
    logging.info("Sending ping to %s...", url)
    response = ping(url)
    logging.info("response code: %s\n", response)


while True:
    send_ping("www.demo.com")
