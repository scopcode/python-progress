class Dog():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sitting.")

    def roll_over(self):
        print(self.name.title() + " is rolling over.")

my_dog = Dog("tomy", 26)
print("My dog's name is " + my_dog.name.title())
print("My dog's age is " + str(my_dog.age))
my_dog.sit()
my_dog.roll_over()