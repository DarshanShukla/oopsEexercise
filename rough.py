"""
class
constructor
inheritance
private
public
protected
abstraction
encaptulations
polysmospsim
package
modules
method overridding
For all the concepts that we have discussed in our class point by point you have ot write
atleast 10 example in each concept
you have to make sure that use ineuron, Students, class, class type, number of courses,
affiliates, blog, internship, jobs as a reference example
"""


# program to illustrate protected access modifier in a class

# super class
class Student:
    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class Geek(Student):

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


# creating objects of the derived class
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.displayDetails()
