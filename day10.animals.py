#ans q37:
#        Inheritance is a concept in object-oriented programming (OOP) that allows one class (called a derived or child class) to acquire the properties
#        and behaviors of another class (called a base or parent class). 
#       Instead of rewriting the same code in every class, you write common functionality once in a parent class and let child classes reuse it. 
#       Without inheritance, code often ends up duplicated.
#ans q38:
#        super() is a function that gives you access to methods of a parent class from within a child class.
#        It's most commonly used to call the parent class's __init__() method so the parent can perform its initialization.
#       What if you forget to call super().__init__()?
#       Then the parent class never gets initialized.
#ans q39:
#        Method overriding is when a child class provides its own implementation of a method that already exists in its parent class.
#        The child class keeps the same method name and signature, but changes the behavior to better suit the specific type of object.
#       A good real-world example is a notification system.
#       Suppose a company needs to send notifications to users. All notifications are sent using a send() method, but the way they are sent depends on the notification type.
#       Every notification has the same purpose—send a message—but each type sends it differently:
#       Email uses an email server.SMS uses a mobile network.Push notifications use services like Firebase or Apple Push Notification service.
#       If every class used the same send() method from the parent, all notifications would behave identically, which wouldn't work. By overriding send(),
#       each subclass provides the correct implementation while keeping the same interface.
#ans q40:
#        Polymorphism means "many forms." In OOP, it allows different objects to respond to the same method call in their own way.
#        example:
#        class Dog:  speak = lambda self: print("Woof")
#        class Cat:  speak = lambda self: print("Meow")
#       for animal in (Dog(), Cat()): animal.speak()
class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        self.alive = True
    def speak(self):
        print(f"{self.name} make a sound.")
    def eat(self, food):
        print(f"{self.name} eats {food}.")
    def sleep(self, hours):
        print(f"{self.name} sleep for {hours}")
    def describe(self):
        status = "Alive" if self.alive else "Not Alive"
        print(f"{self.__class__.__name__}: {self.name}" f"Age: {self.age}, Status: {status}")
        
class Dog(Animal):
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, "Woof")
        self.breed = breed
        self.owner = owner
        self.tricks = []
    def speak(self):
        print(f"{self.name} Barks: {self.sound}! {self.sound}!")
        
    def learn_trick(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} Learned '{trick}")
        
    def fetch(self):
        print(f"{self.name} fetches the ball.")

class Cat(Animal):
    def __init__(self, name, age, color, indoor):
        super().__init__(name, age, "Meow")
        self.color = color
        self.indoor = indoor
    def speak(self):
        print(f"{self.name} Purrs and says {self.sound}")
    def climb(self):
        print(f"{self.name} Climbs a tree.")

class Hourse(Animal):
    def __init__(self, name, age, speed, rider):
        super().__init__(name, age, "Neigh")
        self.speed = speed
        self.rider = rider
    def speak(self):
        print(f"{self.name} neifh loudly. {self.sound}")
    def gallop(self):
        print(f"{self.name} gallop at {self.speed} km/h.")
        
class Bird(Animal):
    def __init__(self, name, age, species, can_fly):
        super().__init__(name, age, "Chirp")
        self.species = species
        self.can_fly = can_fly 
    def speak(self):
        print(f"{self.name} chirp cheerfully!")
    def migrate(self):
        if not self.can_fly:
            raise Exception(f"{self.name} can migrate because cant fly.")
        print(f"{self.name} flies south for winter.")

class Fish(Animal):
    def __init__(self, name, age, water_type, fins):
        super().__init__(name, age, "Blub")
        self.water_type = water_type
        self.fins = fins
    def speak(self):
        print(f"{self.name} blows bubble silently.") 
    def swim(self):
        print(f"{self.name} swim through water.")
        
class Shelter(Animal):
    def __init__(self):
        self.animals = []
    def add_animals(self, animal):
        self.animals.append(animal)
    def remove_animals(self, name):
        self.animals = [animal for animal in self.animals if animal.name != name]
    def list_all(self):
        for animal in self.animals:
            animal.describe()
    def find_by_type(self, animal_class):
        return [animal for animal in self.animals if isinstance(animal, animal_class)]
    def oldest_animal(self):
        if not self.animals:
            return None
        return max(self.animals, key=lambda animal: animal.age) 

dog = Dog("Buddy", 5, "Golden Retriever", "Alice")
cat = Cat("Whiskers", 3, "Black", True)
bird = Bird("Sky", 2, "Parrot", True)
fish = Fish("Nemo", 1, "Saltwater", 4)
horse = Hourse("Thunder", 8, 55, "John")
penguin = Bird("Pingu", 6, "Penguin", False)

dog.learn_trick("Roll_over")
dog.learn_trick("Shake_hands")

bird.migrate()
try:
    penguin.migrate()
except Exception as e:
    print(e)
animals = [dog, cat, bird, fish, horse, penguin]
print("\n--- Polymorphism Demo ---")
for animal in animals:
    animal.speak()
shelter = Shelter()
for animal in animals:
    shelter.add_animals(animal)
print("\n--- Shelter Animals ---")
shelter.list_all()
print("\nOldest Animal:")
shelter.oldest_animal().describe()
print("\nDogs in Shelter:")
for dog in shelter.find_by_type(Dog):
    dog.describe()
print("\n--- Mammals Only (isinstance Demo) ---")
mammls = [ animal for animal in animals if isinstance(animal,(Dog, Cat, Hourse))] 
for mamml in mammls:
    mamml.describe()

    

               