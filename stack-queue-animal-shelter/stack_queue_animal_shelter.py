class AnimalShelter:
    class Animal:
        def __init__(self, species, name):
            """
            Initializes a new Animal instance with the specified species and name.

            Args:
                species (str): The species of the animal.
                name (str): The name of the animal.
            """
            self.species = species
            self.name = name

    def __init__(self):
        """
        Initializes a new instance of the AnimalShelter class.
        """
        self.queue = []

    def print(self):
        """
        Prints the details of all animals in the shelter.
        """
        for animal in self.queue:
            print(f"Animal Type : {animal.species}, Animal Name : {animal.name}")

    def enqueue(self, species, name):
        """
        Adds a new animal to the shelter.

        Args:
            species (str): The species of the animal.
            name (str): The name of the animal.
        """
        animal = self.Animal(species, name)
        self.queue.append(animal)

    def dequeue(self, pref):
        """
        Removes and returns an animal from the shelter based on the given preference.

        Args:
            pref (str): The preferred species of the animal to dequeue.

        Returns:
            Animal or None: The dequeued animal if found, None otherwise.
        """
        selected_animal = None

        for index, animal in enumerate(self.queue):
            if animal.species == pref:
                selected_animal = self.queue.pop(index)
                break

        if selected_animal:
            print(selected_animal.name)

        return selected_animal
