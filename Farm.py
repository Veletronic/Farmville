from Wheat_class import *
from Potato_class import *
from Cow_class import *
from Sheep_class import*

def display():
    print("""
Which crop would you like to grow?

1.Potato
2.Wheat

Please select an option from above""")

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                Valid = True
            else:
                print("Please enter a valid option!")
        except ValueError:
            print("Please enter a valid option!!")
    return choice

def create_crop():
    display()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop

def main():
    new_Crop = create_crop()
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
                
