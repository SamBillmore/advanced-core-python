"""
The code below is almost identical to ex3_part1.

This time, you'll write a new version of `rate_limit`, which accepts an argument
to specify the minimum time there should be between calls. You can copy the
`rate_limit` decorator from exercise 2 as a starting point if you like.

1. Write your new `rate_limit` decorator, which should expect one argument. This
   argument should specify the minimum time (in seconds) allowed between two
   calls to the wrapped function.

2. Uncomment the decorator line above the `send_ping` function. This should
   add a rate limit of one call every 1.75s. Run the script, and make sure that
   the pings are always exactly 1.75s apart.
"""

import logging
import time
import functools

from utils import ping


# TODO: Write your new `rate_limit` decorator here.
class rate_limit:
    def __init__(self, delay):
        self.delay = delay
        self.last_call_time = None

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.last_call_time:
                time_since_last_call = time.time() - self.last_call_time
                if time_since_last_call < self.delay:
                    sleep_time = self.delay - time_since_last_call
                    logging.debug("Sleeping for %.2fs", sleep_time)
                    time.sleep(sleep_time)

            self.last_call_time = time.time()
            return func(*args, **kwargs)
        return wrapper


@rate_limit(1.75)
def send_ping(url):
    logging.info("Sending ping to %s...", url)
    response = ping(url)
    logging.info("response code: %s\n", response)


while True:
    send_ping("http://adding_para.ms")
