class Dog_Breed:
    animal = "Dog"

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed= breed

Leo = Dog_Breed("Leo",4,"Golden Retriever")
Cooper = Dog_Breed("Cooper",7,"Beagle")

print ("Leo is a",Leo.breed,"And he is",Leo.age)
print ("Cooper is a",Cooper.breed,"And he is",Cooper.age)
