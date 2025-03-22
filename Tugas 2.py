from abc import ABC, abstractmethod
import random

class DisneyFilm(ABC):
    @abstractmethod
    def populer_song(self):
        pass

    @abstractmethod
    def character(self):
        pass

    @abstractmethod
    def villain(self):
        pass

class Tangled(DisneyFilm):
    def populer_song(self):
        return "I see the light"

    def character(self):
        return "Rapunzel"

    def villain(self):
        return "Mother Gothel"

class Aladdin(DisneyFilm):
    def populer_song(self):
        return "A Whole New World"

    def character(self):
        return "Aladdin"

    def villain(self):
        return "Jafar"

class Mufasa_The_Lion_King(DisneyFilm):
    def populer_song(self):
        return "I Always Wanted A Brother"

    def character(self):
        return "Mufasa"

    def villain(self):
        return "Scar"
    
print ("\nDisney Film ")
print ("_________________________")
print ("\n1. Tangeld")

tangled = Tangled()
print(f"Popular Song: {tangled.populer_song()}")
print(f"Character: {tangled.character()}")
print(f"Villain: {tangled.villain()}")

print ("\n2. Aladdin")

aladdin = Aladdin()
print(f"Popular Song: {aladdin.populer_song()}")
print(f"Character: {aladdin.character()}")
print(f"Villain: {aladdin.villain()}")

print ("\n3. Mufasa : The Lion King")

mufasa= Mufasa_The_Lion_King()
print(f"Popular Song: {mufasa.populer_song()}")
print(f"Character: {mufasa.character()}")
print(f"Villain: {mufasa.villain()}")