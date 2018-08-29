import random
class Animal:
    """A generic animal"""

    #Constructor
    def __init__(self, growth_r8, food_req, water_req):
        #Set attributes with an initial value

        self._growth = 0
        self._weight = 0
        self._days_growing = 0
        self._growth_r8 = growth_r8
        self._food_req = food_req
        self._water_req = water_req
        self._status = "infant"
        self._type = "Generic"
    
        # _'s before each attribute name indicates they're private.

    def needs(self):
        #returns a dictionary containing light and water requirements
        return {'food requirements' :self._food_req, 'water requirements':self._water_req}

    #Method report to provide info about current state of crop
    def report(self):
        #returns dictionary containing type, status and growth.
        return {'type':self._type, 'status':self._status, 'growth':self._growth, 'days growing':self._days_growing}

    def _update_stat(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self.status = "Mature"
        elif self._growth  > 5:
            self.status = "Young"
        elif self._growth > 0:
            self._status = "infant"

    def grow(self,food,water):
        if food >= self._food_req and water >= self._water_req:
            self._growth += self._growth_r8
        #increments days growing
        self._days_growing += 1
        #Updates status
        self._update_stat()

def auto_grow(animal, days):
    #Grows crop
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    #Gets water and food values from users
    valid = False
    while not valid:
        try:
            water = int(input("Please enter the water value (1-10): "))
            if 1 <= water <= 10: #If the water value is in between 1 and 10
                valid = True
            else:
                print ("Please enter a valid value!")
        except ValueError:
            print("Please enter a valid value!!")
    valid = False
    while not valid:
        try:
            food = int(input("Please enter the light value (1-10): "))
            if 1 <= food <= 10: #If the food value is in between 1 and 10
                valid = True
            else:
                print ("Please enter a valid value!")
        except ValueError:
            print("Please enter a valid value!!")
    #grows Animal
    crop.grow(water,food)

def display():
    print("""1. Nurture manually over 1 day
2. Nurture Automatically over 30 days
3. Report status
4. Quit

Please select an option above""")

def get_menu():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please try again")
        except ValueError:
            print("Please try again")
    return choice

def manage_animal(animal):
    print ("This is the Animal management program")
    print()
    noexit= True
    while noexit:
        display()
        option = get_menu()
        print()
        if option == 1:
            manual_grow(animal)
        elif option == 2:
            auto_grow(animal,30)
        elif option == 3:
            print(animal.report())
        elif option == 4:
            quit()
        elif option == 0:
            noexit= False
            print()
    

def main():
    #Starts the class
    new_animal = animal(1,4,3) 
    manage_animal(new_crop)
    

if __name__ == "__main__":
    main()

