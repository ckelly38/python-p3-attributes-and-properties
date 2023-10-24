#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Dog", breed="Pug"):
        self.setName(name);
        self.setBreed(breed);

    def setName(self, val):
        if (val == None):
            print("Name must be string between 1 and 25 characters.");
        elif (type(val) == str and len(val) > 1 and len(val) < 25):
            self.name = val;
        else: print("Name must be string between 1 and 25 characters.");
        return None;
    
    def getName(self):
        return self.name;

    def setBreed(self, val):
        if (val not in APPROVED_BREEDS):
            print("Breed must be in list of approved breeds.");
        else: self.breed = val;
        return None;

    def getBreed(self): return self.breed;
