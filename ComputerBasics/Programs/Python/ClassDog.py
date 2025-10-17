class Dog:
    # The __init__ method is a constructor, automatically called when a new object is created.
    # 'self' refers to the instance of the class (the object itself).
    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute

    # This is a method (a function defined within a class).
    # It takes 'self' as its first parameter to access the object's attributes.
    def bark(self):
        return f"{self.name} says Woof!"

    def describe(self):
        return f"{self.name} is a {self.breed}."

# Create objects (instances) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
another_dog = Dog("Lucy", "Beagle")

# Access attributes of the objects
print(f"My dog's name is {my_dog.name} and it's a {my_dog.breed}.")
print(f"Another dog's name is {another_dog.name} and it's a {another_dog.breed}.")

# Call methods on the objects
print(my_dog.bark())
print(another_dog.describe())