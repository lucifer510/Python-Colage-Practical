# Write a program to create Class Student and demonstrate the magic Function.
class student():
    def __init__(self, *args):
        print("Now called __init__ magic method, after tha initialised parameters")
        self.name = args[0]
        self.subject = args[1]
        self.marks = args[2]

    def called(self):
        print(self.name)


Student = student("Mihir", "Python", 100)

print("Details are: \n", Student.name, "\n", Student.subject, "\n", Student.marks)
Student.called()


# _add_method adding two object

# Creating a class
class Method_1:
    def __init__(self, *argument):
        self.attribute = argument[0]
        self.attribute2 = argument[1]


# Creating a second class
class Method_2:
    def __init__(self, argument):
        self.attribute = argument
    # creating the instances


instance_1 = Method_1(" Arg", "Welcome")
print(instance_1.attribute)
instance_2 = Method_2("1")
print(instance_2.attribute)

# Adding two attributes of the instances
print(instance_2.attribute + instance_1.attribute)
