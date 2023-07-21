"""
Refactor the code below to extract a new mixin class called LoggerMixin, which
is subclassed by the User class. The LoggerMixin class should provide the
`logger` property, and the `log_info` method.

Run the script to make sure that the code behaviour has not changed.
"""

import logging

logging.basicConfig(level=logging.INFO)


class LoggerMixin:
    @property
    def logger(self):
        return logging.getLogger(self.__class__.__name__)

    def log_info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)


class User(LoggerMixin):
    def __init__(self, name):
        self.name = name
        self.log_info("New user created %s", self.name)


# Create a couple of users to check the logging is working
User("Marlin Brando")
User("Sandra Pollock")
