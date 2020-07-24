"""

Sys Module -

The Sys module contains system specific functionality. We already seen that the sys.argv  list contains the command line arguments.

>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=0, releaselevel='final', serial=0)
>>> sys.version_info.major == 3
True

Loggin Module -


To Explore - Debugging, Handling Command line options, regular expressions

"""

import os
import platform
import logging

if platform.platform().startswith('Windows'):
	logging_file = os.path.join(os.getenv('HOMEDRIVE'),os.getenv('HOMEPATH'), 'test.log' )
else:
	logging_file = os.path.join(os.getenv('HOME'),'test.log')

print("Logging to",logging_file)

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s : %(levelname)s : %(message)s',
filename=logging_file,
filemode='w'
)

logging.debug("start of the program")
logging.info("Doing Something")
logging.warning("Drying now")


