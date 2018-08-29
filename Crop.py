import random
class Crop:
    """A generic food crop"""

    #Constructor
    def __init__(self, growth_r8, light_req, water_req):
        #Set attributes with an initial value

        self._growth = 0
        self._days_growing = 0
        self._growth_r8 = growth_r8
        self._light_req = light_req
        self._water_req = water_req
        self._status = "seed"
        self._type = "Generic"
    
        # _'s before each attribute name indicates they're private.

    def needs(self):
        #returns a dictionary containing light and water requirements
        return {'light requirements' :self._light_req, 'water requirements':self._water_req}

    #Method report to provide info about current state of crop
    def report(self):
        #returns dictionary containing type, status and growth.
        return {'type':self._type, 'status':self._status, 'growth':self._growth, 'days growing':self._days_growing}

    def _update_stat(self):
        if self._growth > 30:
            self._status = "Rotten"
        elif self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self.status = "Mature"
        elif self._growth  > 5:
            self.status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self,light,water):
        if light >= self._light_req and water >= self._water_req:
            self._growth += self._growth_r8
        #increments days growing
        self._days_growing += 1
        #Updates status
        self._update_stat()

def auto_grow(crop, days):
    #Grows crop
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    #Gets water and light values from users
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
            light = int(input("Please enter the light value (1-10): "))
            if 1 <= light <= 10: #If the light value is in between 1 and 10
                valid = True
            else:
                print ("Please enter a valid value!")
        except ValueError:
            print("Please enter a valid value!!")
    #grows crop
    crop.grow(water,light)

def display():
    print("""1. Grow manually over 1 day
2. Grow Automatically over 30 days
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

def manage_crop(crop):
    print ("This is the crop management program")
    print()
    noexit= True
    while noexit:
        display()
        option = get_menu()
        print()
        if option == 1:
            manual_grow(crop)
        elif option == 2:
            auto_grow(crop,30)
        elif option == 3:
            print(crop.report())
        elif option == 4:
            quit()
        elif option == 0:
            noexit= False
            print()
    

def main():
    #Starts the class
    new_crop = Crop(1,4,3) 
    manage_crop(new_crop)
    

if __name__ == "__main__":
    main()
