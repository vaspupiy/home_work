class Dog:
    """Dog model"""

    def __init__(self, name, age):
        """init name, age"""
        self.name = name
        self.age = age

    def sit(self):
        """Dog sit for comand"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Dog roll over"""
        print(self.name.title() + " rolled over!")


my_dog = Dog("Sinta", 6)
print(my_dog.name.title())
print(str(my_dog.age))
my_dog.sit()
my_dog.roll_over()
