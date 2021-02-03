# bmi.py
# A program that calculates somebody's Body Mass Index (BMI)
# The inputs are the person's height in centimetres and weight in kilograms.
# The output  is their weight divided by their height in metres squared.
# Author: Gary moloney

# Promting the user to enter their weight
# Then pasrsing it to an int
# Then assigning it to a variable called weight

weight_CM = int(input("\nEnter weight: "))

# Promting the user to enter their height
# Then pasrsing it to an int
# Then dividing by 100 to convert it to meters
# Then squaring it to convert it to meters squared
# Then assigning it to a variable called weight

height_M2 = ( int(input("\nEnter height: ")) / 100 ) ** 2

# Dividing the weight var by the height var
# Then rounding it to one decimal place to produce the final BMI
# Then printing out the BMI

print('\n BMI is {} \n'.format(round(weight_CM/height_M2,1)))