class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed}."

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Bulldog(Dog):
    def speak(self, sound="Woof"):
        return super().speak(sound)


class Dachshund(Dog):
    def speak(self, sound="Yap"):
        return super().speak(sound)


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


mikey = Bulldog("Mikey", 6, "Bulldog")
bruno = Dachshund("Bruno", 3, "Dachshund")
bella = GoldenRetriever("Bella", 2, "Golden Retriever")

print(mikey)
print(bruno)
print(bella)

print(mikey.speak())
print(bruno.speak())
print(bella.speak())
