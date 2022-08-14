class House():
    """description house"""
    def __init__(self, street, number):
        self.street = street
        self.number = number
        self.age = 0
    
    def build(self):
        """build house"""
        print("House on street " + self.street + " number " + str(self.number) + " Done!")

    def age_of_house(self, year):
        """house age"""
        self.age += year

MyHouse = House("Гагарина", 95)

print(MyHouse.number)
MyHouse.build()
MyHouse.age_of_house(5)
print(MyHouse.age)


class ProspectHouse(House):
    """house on the prospect"""
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect

PrHouse = ProspectHouse("Гвардейский", 9)
print(PrHouse.prospect)