class Parrot:
    species = "Bird"

    def __init__ (self,name,age):
        self.name = name
        self.age = age

Blu = Parrot("Blu",6)
Woo = Parrot("Woo",7)

print ("Blu is a {}".format(Blu.species))
print ("Woo is a",Woo.species)

print ("{} is {} years old.".format(Blu.name,Blu.age))
print ("{} is {} years old.".format(Woo.name,Woo.age))