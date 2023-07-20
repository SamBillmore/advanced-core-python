"""
The code in this script calls the same `ping` function as exercise 2, which
either returns a status code, or raises an error.

1. Run this script - you should see a repeated prompt, asking you to hit a key.
   This will repeat until a ping() call errors.

2. This script imports three decorators:
     * catch_errors - which you wrote in exercise 3
     * log_duration - which logs how long a function takes to run
     * debug        - which logs when a function is called, and what it returns

     Use these three decorators on the `get_log_level` and `check_connection`
     functions below, to give debugging information about how the program runs,
     and catch any errors that are thrown.

3. Run the script again, and take a look at the output. Does the order of the
   decorators matter?

4. Without editing any other files, use all three decorators to add
   functionality to the `ping` function before it gets called in
   `check_connection`.
"""

import logging

from utils import ping, log_duration, debug
from ex3_arguments_and_return_values import catch_errors


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Part 4:
# ping = debug(ping)


@debug
def get_log_level(status_code):
    if status_code == 200:
        level, message = logging.INFO, "Ping successful"
    else:
        level, message = logging.WARNING, f"Ping unsuccessful {status_code}"
    return level, message


# Order:
@debug  # Only used in development and will be commented out in production
@log_duration  # Don't want differences in duration depending whether debug is being used
@catch_errors  # Last as don't want to catch errors in decorators
def check_connection():
    status_code = ping()
    if status_code is None:
        raise ValueError("Invalid Status Code")

    log_level, log_message = get_log_level(status_code=status_code)
    logging.log(log_level, log_message)
    return log_level == logging.INFO


if __name__ == "__main__":
    while True:
        input("\nPress a key to send a ping...")
        check_connection()
