class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __add__(self, other):
        if isinstance(other, Person):
            return self.age + other.age
        return NotImplemented

    def __len__(self):
        return len(self.name)


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# __str__: Custom string representation
print(person1)  

# __add__: Add ages of two persons
total_age = person1 + person2
print(f"Total age: {total_age}") 

# __len__: Length of the name
print(len(person1))  
