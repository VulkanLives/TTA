class Point:

    def __new__(cls, *args, **kwargs):

        print("1. Create a new instance of Point.")

        return super().__new__(cls)


    def __init__(self, x, y):

        print("2. Initialize the new instance of Point.")

        self.x = x

        self.y = y


    def __repr__(self) -> str:

        return f"{type(self).__name__}(x={self.x}, y={self.y})"


# Here’s a breakdown of what this code does:
#
#     Line 3 defines the Point class using the class keyword followed by the class name.
#
#     Line 4 defines the .__new__() method, which takes the class as its first argument. Note that using cls as the name of this argument is a strong convention in Python, just like using self to name the current instance is. The method also takes *args and **kwargs, which allow for passing an undefined number of initialization arguments to the underlying instance.
#
#     Line 5 prints a message when .__new__() runs the object creation step.
#
#     Line 6 creates a new Point instance by calling the parent class’s .__new__() method with cls as an argument. In this example, object is the parent class, and the call to super() gives you access to it. Then the instance is returned. This instance will be the first argument to .__init__().
#
#     Line 8 defines .__init__(), which is responsible for the initialization step. This method takes a first argument called self, which holds a reference to the current instance. The method also takes two additional arguments, x and y. These arguments hold initial values for the instance attributes .x and .y. You need to pass suitable values for these arguments in the call to Point(), as you’ll learn in a moment.
#
#     Line 9 prints a message when .__init__() runs the object initialization step.
#
#     Lines 10 and 11 initialize .x and .y, respectively. To do this, they use the provided input arguments x and y.
#
#     Lines 13 and 14 implement the .__repr__() special method, which provides a proper string representation for your Point class.
