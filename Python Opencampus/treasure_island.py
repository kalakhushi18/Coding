# print("Welcome to Treasure Island!!!")

# print("Your mission is to find the Treasure")

# direction = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right' ")


coord_str = "X3Y4"

def find_coord(coord_str):
    coord_str = coord_str.lower()
    for i, val in enumerate(coord_str):
        print(val)
        if val == 'x':
            if i+1 < len(coord_str):
                x_value = int(coord_str[i + 1])
        elif val == 'y':
            if i+1 < len(coord_str):
                y_value = int(coord_str[i + 1])
    print(tuple((x_value,y_value)))

find_coord(coord_str=coord_str)



        


