import re

# To check the pattern for a floating number
float_num_pattern = "([0-9]*[.])?[0-9]+"
num_pattern = '^[0-9]+$'
valid_bill_amt = False
valid_tip_amt = False
valid_num_of_people = False
pay_amt = 0


print("Hello! We calculate your Split!!!\n")

while not valid_bill_amt:
    total_bill_amt = input('What was the total bill? $')
    #checking bill amt validity
    if bool(re.match(float_num_pattern, total_bill_amt)):
        valid_bill_amt = True
        total_bill_amt = float(total_bill_amt)
    else:
        valid_bill_amt = False
        print('Enter correct bill amount')

while not valid_tip_amt:
    tip_amt = input('How much tip do you want to give?10, 15 or 20? $')
    #checking tip amt validity
    if bool(re.match(float_num_pattern, tip_amt)):
        tip_amt = float(tip_amt)
        if tip_amt in [10,15,20]:
            valid_tip_amt = True
            tip_amt = float(tip_amt)
        else:
            valid_tip_amt = False
            print('Please enter only from the above mentioned tips.')
    else:
        valid_tip_amt = False
        print('Enter correct tip amount')

while not valid_num_of_people:
    num_of_people = input('How many people to split the Bill? ')
    #checking num of people validity
    if bool(re.match(num_pattern, num_of_people)):
            valid_num_of_people= True
            num_of_people = float(num_of_people)
    else:
        valid_num_of_people = False
        print('Enter correct number of people.')


if num_of_people == 0:
    pay_amt = total_bill_amt + tip_amt
    print(f'Total bill to be paid is: ${pay_amt} ')
else:
    pay_amt = ((total_bill_amt + tip_amt) / num_of_people )
    print(f'Total bill to be paid by each person is: ${pay_amt} ')

