# 3-6: Create the data structures to maintain a system for an animal shelter where an adopter can receive 
# either the "oldest" (based on arrival time) animal, the oldest dog available, or the oldest cat available.
# The data structures should be able to handle the following operations: enqueue, dequeueAny, dequeueDog 
# and dequeueCat.

class AnimalShelter:
    def __init__(self):
        self.animals = []

    def enqueue(self, animal):
        self.animals.append(animal)

    def dequeueAny(self):
        return self.animals.pop(0)

    def dequeueDog(self):
        for animal in self.animals:
            if animal.isDog():
                return self.animals.pop(self.animals.index(animal))
        return None

    def dequeueCat(self):
        for animal in self.animals:
            if animal.isCat():
                return self.animals.pop(self.animals.index(animal))
        return None

    def __str__(self):
        return str([str(x) for x in self.animals])

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def isDog(self):
        if self.species == 'dog':
            return True
        return False

    def isCat(self):
        if self.species == 'cat':
            return True
        return False

    def __str__(self):
        if self.isDog():
            return f'Ruff! I\'m {self.name}'
        elif self.isCat():
            return f'Meow! I\'m {self.name}'
        else:
            return f'??? I\'m {self.name}'

# Test solution
if __name__ == "__main__":
    shelter = AnimalShelter()
    # Initialize with 4 dogs and 2 cats
    shelter.enqueue(Animal('Fido', 'dog'))
    shelter.enqueue(Animal('Larry', 'dog'))
    shelter.enqueue(Animal('Bill', 'cat'))
    shelter.enqueue(Animal('Pablo', 'dog'))
    shelter.enqueue(Animal('Terry', 'cat'))
    shelter.enqueue(Animal('Ladybird', 'dog'))

    print(shelter)

    print('I want a cat, please...')
    print(shelter.dequeueCat())  # Should give the oldest cat, Bill

    print('I want a dog, please...')
    print(shelter.dequeueDog())  # Should give the oldest dog, Fido

    print('I want either a dog or a cat, please...')
    print(shelter.dequeueAny())  # Should give the oldest animal left, Larry (a dog)

    print(shelter)  # Should have 3 animals left, 1 cat and 2 dogs



