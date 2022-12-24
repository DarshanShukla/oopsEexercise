"""
The members of a class that are declared protected are only accessible to a class derived from it. Data members of a
class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class.
"""

import logging
logging.basicConfig(filename = "private.log", level = logging.DEBUG, format="%(levelname)s - %(asctime)s - %(message)s")
logging.warning

class mouse:
    logging.info("protected class 1")
    def __init__(self,one,two, three, four, five ):
        """NICK NAMES OF MOUSE"""
        try:
            self._one = one
            self._two = two
            self._three = three
            self._four = four
            self._five = five
        except Exception as e:
            logging.info(e)

mushak = mouse("nick", "rick", "mick", "yuvraj", "g2")
print(mushak._three)


