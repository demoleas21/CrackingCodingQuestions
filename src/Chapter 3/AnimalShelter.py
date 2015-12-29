"""3.6 Animal Shelter"""

class Queue(object):
    """Queue Data Structure"""
    def __init__(self):
        self.container = []

    def push(self, data):
        """Adds data to queue"""
        self.container.append(data)

    def pop(self):
        """Removes the top element"""
        animal = (self.container[0])
        del self.container[0]
        return animal

    def pop_cat(self):
        """Removes the top cat"""
        i = 0
        while i < len(self.container):
            for animal in self.container[i]:
                if animal == 'cat':
                    cat = (self.container[i])
                    del self.container[i]
                    return cat
            i = i + 1

    def pop_dog(self):
        """Removes the top dog"""
        i = 0
        while i < len(self.container):
            for animal in self.container[i]:
                if animal == 'dog':
                    dog = (self.container[i])
                    del self.container[i]
                    return dog
            i = i + 1

    def peek(self):
        """Display the top of queue"""
        return self.container[0]

    def size(self):
        """Display size of queue"""
        return len(self.container)

    def is_empty(self):
        """Informs if stack is empty"""
        return self.container == []

def main():
    """Main function"""
    animal_shelter = Queue()
    animal_shelter.push({'cat':'Tammy'})
    animal_shelter.push({'dog':'Sir Barks-a-lot'})
    animal_shelter.push({'dog':'Sparky'})
    animal_shelter.push({'dog':'Coconut'})
    animal_shelter.push({'cat':'Fluffy'})
    animal_shelter.push({'cat':'Mustache'})
    animal_shelter.push({'dog':'Snoopy'})

    animal = input("\nWould you like a cat, dog, or either? ")
    if animal == 'cat':
        print(animal_shelter.pop_cat())
    elif animal == 'dog':
        print(animal_shelter.pop_dog())
    elif animal == 'either':
        print(animal_shelter.pop())
    else:
        print("Error! Please try again")


if __name__ == "__main__":
    main()
