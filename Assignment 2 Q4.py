# Dog class
class Dog:
    def make_sound(self):
        return "Woof! "


# Cat class
class Cat:
    def make_sound(self):
        return "Meow! "


# Function that expects any object with make_sound()
def process_sound(sound_object):
    print("Sound:", sound_object.make_sound())


# Example usage
dog = Dog()
cat = Cat()

process_sound(dog)   # Works with Dog
process_sound(cat)   # Works with Cat

