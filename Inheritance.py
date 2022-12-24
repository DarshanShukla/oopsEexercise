

import logging

logging.basicConfig(filename="Inheritance.log", level=logging.DEBUG,format="%(levelname)s - %(asctime)s - %(message)s")

"""first question of inheritance"""
class class1:
    def school(self):
        try:
            print("place to learn")
        except Exception as e:
            logging.info(e)

    def geeta(self):
        try:
            print("learn wisdom")
        except Exception as e:
            logging.info(e)

class job(class1):
    def ineuron_to_job(self):
        try:
            print("this will show all the information in ineuron class")
        except Exception as e:
            logging.info(e)

i = job()
i.geeta()


""""""