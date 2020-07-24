"""
Decorators -

Decorators are a shortcut to applying wrapper functions, This is helpful to "wrap" functionality with the same code over and over again. For example,we created a retry decorator for myself that i can just apply to any function and if any exception is thrown during the run , it is retried again, till a maximum of 5 times and with a delay between each retry. This is especially useful for the situations when you are trying to make a network call to a remote computer.

"""

from time import sleep
from functools import wraps
import logging
loggin.basicConfig()
log = logging.getLogger("retry")


