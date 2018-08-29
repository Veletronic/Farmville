from Crop import *

class Potato(Crop): #Potato inherits from crop
    """A potato crop"""

    #Constructor
    def __init__(self):
        #Call the parent class constructor with default value 4 pot
        #Growth rate =1; light requirement = 3; water requirement = 6
        super().__init__(1,3,6)
        self._type = "Potato" #basic sub-class

    #Overrides growth method for subclasses
    def grow(self,light,water):
        if light>= self._light_req and water >= self.water_req:
            if self._status == "Seedling" and water > self._water_req:
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
              #Creates potato
              potato_crop = Potato()
              print(potato_crop.report())
              #manually grows
              manual_grow(potato_crop)
              print(potato_crop.report())
if __name__ == "__main__":
    main()
    
