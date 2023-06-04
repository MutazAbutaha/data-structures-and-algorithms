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
            self.next = None

    def __init__(self):
        """
        Initializes a new instance of the AnimalShelter class.
        """
        self.front = None
        self.back = None

    def print(self):
        """
        Prints the details of all animals in the shelter.
        """
        current = self.front
        while current is not None:
            print(f"Animal Type: {current.species}, Animal Name: {current.name}")
            current = current.next

    def enqueue(self, species, name):
        """
        Adds a new animal to the shelter.

        Args:
            species (str): The species of the animal.
            name (str): The name of the animal.
        """
        animal = self.Animal(species, name)
        if self.back is None:
            self.front = animal
            self.back = animal
        else:
            self.back.next = animal
            self.back = animal

    def dequeue(self, pref):
        """
        Removes and returns an animal from the shelter based on the given preference.

        Args:
            pref (str): The preferred species of the animal to dequeue.

        Returns:
            Animal or None: The dequeued animal if found, None otherwise.
        """
        selected_animal = None
        current = self.front
        previous = None

        while current is not None:
            if current.species == pref:
                selected_animal = current
                if previous is None:
                    self.front = current.next
                else:
                    previous.next = current.next

                if current == self.back:
                    self.back = previous

                break

            previous = current
            current = current.next

        if selected_animal:
            print(selected_animal.name)

        return selected_animal

ani = AnimalShelter()
ani.enqueue("dog", "Mossberg")
ani.enqueue("cat", "Mirabel")
ani.enqueue("dog", "Mossberg")
ani.enqueue("cat", "Mirabel")
ani.print()
ani.dequeue("cat")
ani.print()

