import time
import re

# This program generates a band name based on city and pet name input.
# Since city name must be only alphabets thus it is checked, else it is printed

print("Brand Name Generator \n")
print("Hello " + input("What is your Name?"))
valid_city_name = False

while not valid_city_name:
    birth_city = input("What is your Birth City?\n")
    if bool(re.match('^[a-zA-Z]+$', birth_city)):
        valid_city_name = True
        pet_name = input('What is your pet name?\n')
        band_name = birth_city + ' ' + pet_name
        print('Loading Band name...\n')
        time.sleep(0.2)
        print(f'An exciting Band Name is {band_name.upper()}!!!')
    else:
        valid_city_name = False
        print("Please input the right city name\n")


     
         




