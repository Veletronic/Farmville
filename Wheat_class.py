from Crop import *

class Wheat(Crop):
    """A wheat crop"""

    def __init__(self):
        #Growth rate =1; light requirement = 5; water requirement = 10
        super().__init__(1,5,10)
        self._type = "Wheat"

def main():
    wheat_crop = Wheat()
    print(wheat_crop.report())
    #Manual growth
    manual_grow(wheat_crop)

if __name__ == "__main__":
    main()
