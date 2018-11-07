"""
3.6 Animal Shelter.

An animal shelter, which holds only dogs and cats, operates on a strictly
"first in, first out" basis. People must adopt either the "oldest"(based on
arrival time) of all animals at the shelter, or they can select whether they
would prefer a dog or a cat(and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data
structures to maintain this system and implement operations such as enqueue,
dequeueAny, dequeueDog, and dequeueCat. You may use built-in LinkedList data
structure.
"""


class AnimalQueue:
    """Class for cats and dogs queue."""

    def __init__(self):
        """Init method."""
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, animal, dog):
        """Method to add a item to the end of the queue."""
        self.order += 1
        if dog:
            self.dogs.append((animal, self.order))
        else:
            self.cats.append((animal, self.order))

    def dequeue_any(self):
        """Dequeue oldest animal."""
        if self.dogs[-1][1] > self.cats[-1][1]:
            self.dequeue_dogs()
        else:
            self.dequeue_cats()

    def dequeue_dogs(self):
        """Dequeue oldest dog."""
        del self.dogs[0]

    def dequeue_cats(self):
        """Dequeue oldest dog."""
        del self.cats[0]
