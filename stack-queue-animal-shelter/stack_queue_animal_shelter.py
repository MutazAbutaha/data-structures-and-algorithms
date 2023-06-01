class AnimalShelter:
    class Animal:
        def __init__(self, species, name):
            self.species = species
            self.name = name

    def __init__(self):
        self.queue = []

    def print(self):
        for animal in self.queue:
            print(f"Animal Type : {animal.species}, Animal Name : {animal.name}")

    def enqueue(self, species, name):
        animal = self.Animal(species, name)
        self.queue.append(animal)

    def dequeue(self, pref):
        selected_animal = None

        for index, animal in enumerate(self.queue):
            if animal.species == pref:
                selected_animal = self.queue.pop(index)
                break

        if selected_animal:
            print(selected_animal.name)

        return selected_animal
