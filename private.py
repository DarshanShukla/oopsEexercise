import logging

logging.basicConfig(filename = "private.log", level = logging.DEBUG, format= "%(levelname)s - %(asctime)s - %(message)s" )
logging.warning("This will logged a file")

class flat:
    logging.info("information about a flat")
    def __init__(self, size, rooms, location):
        """INFO ABOUT A FLAT"""
        try:
            self.size = size
            self.room = __room
            self.location = _location
        except Exception as e:
            logging.exception(e)

dwarikaparisar = flat("3000sq", 6, "main city")
print(dwarikaparisar.size)
print(dwarikaparisar._flat.__room)