from Potato_class import*
from Wheat_class import*
from Sheep_class import*
from Cow_class import*

class Field:
    """Simulates a field that can contain x amount of animals and crops"""

    #Constructor
    def __init__(self,max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self, crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self, animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

def display_crops(crop_list):
    print()
    print("The following crops are growing:")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos,crop.report()))
        pos += 1



def display_animals(animal_list):
    print()
    print("The following animals are in this field")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos,animal.report()))
        pos += 1

def select_crops(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def select_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select an animal: "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def harvest_crop_field(field):
    display_crops(field._crops)
    selected_crop = select_crops(len(field._crops))
    return field.harvest(selected_crop)

def remove_animal_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field.animals))
    return field.remove.animal_field(selected_animal)


def main():
    new_field = Field(5,2)
    new_field.plant_crop(Wheat())
    new_field.add_animal(Sheep())
    new_field.add_animal(Cow())
    new_field.plant_crop(Potato())
    new_field.harvest(0)
    new_field.remove_animal(0)
    harvest_crop_field(new_field)
    print(new_field._crops)
    remove_animal_field(new_field)
    print(new_field._animals)
    


if __name__ == "__main__":
    main()
