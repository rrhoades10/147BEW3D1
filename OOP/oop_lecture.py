# CLASSES
# blueprints for objects that we create from the class

# class defines that we're building a class
class OfficeBuilding:
    # attributes - variables in a class
    # special method denoted by the double underscores
    # initializes the attributes for the class
    # this gets called every time we create a new object from a class
    # self refers to the objects created from this class
    def __init__(self, floors, offices):
        # setting class attributes
        # self eventually becomes the object
        self.floors = floors        
        self.offices = offices

    # methods - functions in a class


# instantiating our class
building1 = OfficeBuilding(5, 10)
# self.floors
# building1.floors = 5
# self.offices
# building1.offices = 10
# accessing floors
print(building1.floors)

# instantiating with keyword arguments
# new instance of the class
building2 = OfficeBuilding(offices = 16, floors = 11)
print(building2.floors)
print(building2.offices)

# default parameters and attributes in a class
class Dog:
    #                                default parameter for the class
    def __init__(self, legs, sound, color = "brown"):
        self.legs = legs
        self.sound = sound
        self.color = color

eyo = Dog(4, "roooo")
print(eyo.sound, eyo.color)


#                        overrides the default paramter
shadow = Dog(4, "WOóF", "black")
print(f"Karen's European dog's name is Shadow and he is {shadow.color}")

# setting a defualt attribute within the init
class Dog:
    #                               
    def __init__(self, sound, color):
        self.legs = 4 #set a default attribute - this can only be changed through the object
        # it doesnt change when we instantiate because theres no option to take an argument for this
        # specific attribute
        self.sound = sound
        self.color = color

chance = Dog("Woof", "White with brown spots")
print(chance.legs)
print(chance.sound)


# class methods
class OfficeBuilding:
    # attributes - variables in a class
    # special method denoted by the double underscores
    # initializes the attributes for the class
    # this gets called every time we create a new object from a class
    # self refers to the objects created from this class
    def __init__(self, floors, offices):
        # setting class attributes
        # self eventually becomes the object
        self.floors = floors        
        self.offices = offices
    
    # methods - functions in a class
    # functions that only objects of the class have access to
    # all class methods will take in self - referencing the objects created from this class
    def open_doors(self):
        print("The doors have been opened. Please come in and get to work....or else")

building3 = OfficeBuilding(20, 30)
# accessing attributes from the class
print(building3.floors)
print(building3.offices)
# calling methods from within a class
building3.open_doors()

# using methods to interact with and change class attributes
class ParkingGarage:
    def __init__(self, parking_spots):
        self.parking_spots = parking_spots #30
        # default class attribute
        self.vip_list = []

    # method to park a car and reduce the number of available parking spots
    def park_car(self):
        print("Parking car....")
        self.parking_spots -= 1
        print(f"Car parked...spots remaining {self.parking_spots}")

    # method for car to exit and increase the available parking spots
    def exit_garage(self):
        print("Leaving garage...")
        self.parking_spots += 1
        print(f"Have a nice day! Remaining spots {self.parking_spots}")

    # view number of available parking spots
    def check_spots(self):
        print(f"There are {self.parking_spots} spots available. ")
#                 taking an additional parameter for a class method
    def vip_park(self, vip):
        print(f"We're parking {vip}'s car. Please be careful")
        self.vip_list.append(vip)
        self.parking_spots -= 1

# instantiating our garage
super_cool_garage = ParkingGarage(30)
# viewing the number of available parking spots
super_cool_garage.check_spots()
# park a car and reduce the number of available parking spots
super_cool_garage.park_car()
super_cool_garage.park_car()
super_cool_garage.park_car()
super_cool_garage.park_car()
super_cool_garage.vip_park("Obama")
super_cool_garage.check_spots()
super_cool_garage.exit_garage()
super_cool_garage.exit_garage()
super_cool_garage.exit_garage()
super_cool_garage.exit_garage()
super_cool_garage.exit_garage()
# viewing vip parking
print(super_cool_garage.vip_list)
print(super_cool_garage.__dict__)

# create a class for a bus
# an attribute for seats
# methods to pick up and drop off passengers to change the number of seats available
# if you're feelin SAUCY change the bus driver
# if youre feelin EXTRA SAUCY change the color of the bus


# Difference class attributes and instance specific attributes
class Dog:
    species = "Canine" #class attribute - shared across all instances of the class
    number_of_dogs = 0

    def __init__(self, name, sound, color): #instance attributes which are unique to the individual instances
        self.name = name
        self.sound = sound
        self.color = color
        Dog.number_of_dogs += 1
        print(Dog.number_of_dogs)

mutt = Dog("Eyo", "Rooo", "Light brown")
doberman = Dog("Shadow", "WOóF", "Black")
golden_retriever = Dog("Luka", "Woof", "Gold")
print(mutt.name)
print(doberman.name)
print(golden_retriever.name)
print(mutt.species)
print(doberman.species)
print(golden_retriever.species)
golden_retriever.species = "Cat?"
print(golden_retriever.species)
print(mutt.species)
print(doberman.species)
print(Dog.species)
Dog.species = "Not a cat"
print(golden_retriever.species)
print(mutt.species)
print(doberman.species)
# print(Dog.species)
another_dog = Dog("Lassie", "bark", "white and stuff")
print(golden_retriever.number_of_dogs)
print(mutt.number_of_dogs)
print(doberman.number_of_dogs)

print(mutt.name)

# .__dict__ on a class object to get a dictionary representation of that object
print(mutt.__dict__)
# turning a class object into a dictionary

print(super_cool_garage.__dict__)