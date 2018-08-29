from Animal import *

class Cow(Animal): #Cow inherits from Animal
    """A cow"""

    #Constructor
    def __init__(self):
        #Call the parent class constructor with default value
        #Growth rate =1; food requirement = 6; water requirement = 8
        super().__init__(1,6,8)
        self._type = "Cow" #basic sub-class

    #Overrides growth method for subclasses
    def grow(self,food,water):
        if food>= self._food_req and water >= self.water_req:
            if self._status == "infant" and water > self._water_req:
                self._growth += self._growth_r8
            elif self._status == "Young" and water >self._water_req:
                self._growth += self._growth_r8 * 1.25
            else:
                self._growth += self._growth_r8
            #Increments days
            self._days_growing += 1
            #Status update
            self._update_status()

def main():
              #Creates cow
              sheep_animal = Sheep()
              print(sheep_crop.report())
              #manually grows
              manual_grow(sheep_animal)
              print(sheep_animal.report())
if __name__ == "__main__":
    main()
