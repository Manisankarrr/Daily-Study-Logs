
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.brand} {self.model} year {self.year}"
    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year
    def __lt__(self, other):
        return self.year < other.year
    def __gt__(self, other):
        return self.year < other.year
    def __add__(self,other):
        return self.year + other.year
    def __contains__(self, keyword):
        return keyword in self.brand
    def __getitem__(self,key):
        if key == "model":
            return self.model
        elif key == "brand":
            return self.brand
        else:
            raise ValueError("Wrong nigga")
    
    
 
car1 = Vehicle("hyundai", "Verna", 2020)
car2 = Vehicle("hyundai", "i20", 2021)

print(car1)
print(car1 == car2)
print(car1 < car2)
print(car1 + car2)
print("hyundai" in car1)
print(car2['mode'])