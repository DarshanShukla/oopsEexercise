import logging
logging.basicConfig(filename="public.log", level= logging.DEBUG, format= "%(levelname)s - %(asctime)s - %(message)s")
logging.warning("This will logged to a file")


# program to illustrate public access modifier in a class
"""public class 1st example"""
class Geek:
    logging.info("public class 1st example")
    # constructor
    def __init__(self, name, age):
        logging.info("public data members")
        try:
            self.geekName = name
            self.geekAge = age

        except Exception as e:
            logging.info(e)


    def displayAge(self):
        logging.info("public member function")
        try:
            # accessing public data member
            print("Age: ", self.geekAge)

        except Exception as e:
            logging.info(e)

# creating object of the class
obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.displayAge()



class colors:
    """NAMES OF COLORS AND COLOR PRODUCTS """
    try:
        logging.info("NAMES OF COLORS AND COLOR PRODUCTS")
        def __init__(self, c1, c2, c3, c4):
            self.c1 = c1
            self.c2 = c2
            self.c3 = c3
            self.c4 = c4
    except Exception as e:
        logging.info(e)

    try:
        logging.info("DISPLAY COLORS")
        def display_rang(self):
            print("The color name is :", self.c1)
    except Exception as e:
        logging.info(e)

names_of_color = colors("red", "blue", "pink", "white")

print("Names: ", names_of_color.c1 )
print("name :", names_of_color.c2, names_of_color.c3)