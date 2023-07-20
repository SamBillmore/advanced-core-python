"""
The code below uses a StatusMonitor class, which uses a separate thread to send
regular pings in the background when `run()` is called. It stops when its
`stop()` method is called.

1. Run this script. You should see that regular pings are being sent to three
   separate services. If you hit Enter the pings are meant to stop (the bottom
   three lines of this script), but they don't because
   `StatusMonitor.all_instances` does not yet work.

2. Write a class decorator called `register_instances`. This should modify a
   class so that:
       * It has a class attribute called `all_instances` that is a list
       * Each time a new instance is created, it is appended to `all_instances`

3. Use `register_instances` to decorate the `StatusMonitor` class. Run the
   script again, and check that when you hit Enter, the pings all stop.
"""

import logging
import threading

from utils import ping

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# TODO: write a decorator called register_instances, and use it to add an
# `all_instances` attribute to the StatusMonitor class.
def register_instances(cls):
    cls.all_instances = []  # A list that is connected with each instance of the class
    original_init = cls.__init__

    def __new_init__(self, *args, **kwargs):
        cls.all_instances.append(self)
        original_init(self, *args, **kwargs)

    cls.__init__ = __new_init__
    return cls



@register_instances
class StatusMonitor:
    def __init__(self, url):
        self.url = url
        self.stopped = False

    def stop(self):
        self.stopped = True

    def run(self):
        if not self.stopped:
            if ping(self.url) == 200:
                logging.info("   Service %s healthy", self.url)
            else:
                logging.warning("Service %s unavailable", self.url)
            # Call self.run again in 2s in a new thread (so it doesn't block)
            threading.Timer(2, self.run).start()


# Start 3 status monitors running (pings are run in threads to avoid blocking)
StatusMonitor("/async_queue").run()
StatusMonitor("/account").run()
StatusMonitor("/scheduler").run()


input("\n\tPress Enter to stop all pings\n\n")
for pinger in StatusMonitor.all_instances:
    pinger.stop()
