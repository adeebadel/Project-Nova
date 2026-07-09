class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def birthday(self):
        self.age = self.age + 1

    def bark(self):
        print("Woof! Woof!")

    def show(self):
        print("\n----- DOG DETAILS -----")
        print("Name :", self.name)
        print("Breed :", self.breed)
        print("Age :", self.age)


dog1 = Dog("Bruno", "Labrador", 3)
dog2 = Dog("Rocky", "German Shepherd", 5)

dog1.show()
dog1.bark()
dog1.birthday()
dog1.show()

dog2.show()
dog2.bark()
dog2.birthday()
dog2.show()


# 2nd one

class MobilePhone:

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def charge(self):
        self.battery = 100

    def use(self):
        self.battery = self.battery - 10

    def show(self):
        print("\n----- PHONE DETAILS -----")
        print("Brand :", self.brand)
        print("Battery :", self.battery, "%")


phone = MobilePhone("Samsung", 70)

phone.show()

phone.use()
phone.show()

phone.charge()
phone.show()