'''
It defines attributes(data) and methods(function) to operate on that data
'''
class car:
    '''
    Constructor (__init__) to initialize object properties
    '''
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
# methods to display car details
    def display(self):
        print(f"car: {self.brand}, Model: {self.model}, Year : {self.year} ")

Car1 = car("Rolls-Royce","Opulence",2023)
Car2 = car("Bugatti","La Voiture Noire",2019)
print(Car1.brand)
Car1.display()