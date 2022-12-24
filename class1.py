"""use ineuron, Students, class, class type, number of courses,
affiliates, blog, internship, jobs as a reference example"""

"""CLASS AND CONSTRUCTOR(__init__)"""

import logging

logging.basicConfig(filename="cons_log.log", level=logging.DEBUG, format="%(levelname)s - %(asctime)s - %(message)s ")
logging.warning('This will get logged to a file')

class students:
    logging.info("solving questions of constructor")

    def __init__(self, name, roll_no, total):
        """TRY TO ADD STUDENTS IN CONSTRUCTOR FORMAT"""
        logging.info("adding students details")
        try:
            self.name = name
            self.roll_num = roll_no

            self.total = total

        except Exception as e:
            logging.info(e)

lekhani = students("lekhani shukla", 26, 100)
darshan = students("darshan shukla", 8, 50)

print(lekhani.name)



class ineuron:
    """ADDING VEHICLE INFO IN A CLASS"""
    logging.info("Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.")
    try:
        def __init__(self,max_speed,mileage):
            self.max_speed = max_speed
            self.mileage = mileage

    except Exception as e:
        logging.exception(e," enter itersble collections")
royalenfield = ineuron(100,40)
print(royalenfield.mileage)
print(royalenfield.max_speed)



class class1:
    """PASSING EMPTY CLASS"""
    logging.info("passing a empty class named class1")
    try:
        pass
    except Exception as e:
        logging.exception(e)
class_1a = class1
print(class_1a)



class class_type1:
    """CREATE A CHILD CLASS BUS THAT WILL INHERIT ALL THE VARIABLES AND METHODS OF class_type1 CLASS"""
    logging.info("create a child class that has values of ineuron class")
    try:
        def __init__(self,max_speed, mileage):
            self.max_speed = max_speed
            self.mileage = mileage
    except Exception as e:
        logging.exception(e)
class baby_class_type1(class_type1):
    pass
auto_wala = baby_class_type1(40,45)
print(auto_wala.max_speed)
print(auto_wala.mileage)



class number_of_courses:
    """how many number of courses ineuron has"""
    logging.info("information of courses ineuron has")
    try:
        def __init__(self,c1,c2,c3,c4,c5):
            self.c1 = c1
            self.c2 = c2
            self.c3 = c3
            self.c4 = c4
            self.c5 = c5
    except Exception as e:
        logging.exception(e)
vishay = number_of_courses("data_science","java","data_analytics","python","machine_learning")
print(vishay.c2)



class affiliates:
    """what are the services affiliates to the bank"""
    logging.info("information about bank servies")
    try:
        def __init__(self,s1,s2,s3,s4):
            self.s1 = s1
            self.s2 = s2
            self.s3 = s3
            self.s4 = s4
    except Exception as e:
        logging.exception(e)
ICICI = affiliates("deposit_of_money", "give_loan", "medium_of_trade", "consultancy")
print(ICICI.s1)



class blog:
    """youtube blogging benefits"""
    logging.info("print youtube ")
    try:
        def __init__(self,i1,i2,i3):
            self.i1 = i1
            self.i2 = i2
            self.i3 = i3
    except Exception as e:
        logging.exception(e)
youtube = blog("money","fame", "communication skills")
print(youtube.i1)


print("")