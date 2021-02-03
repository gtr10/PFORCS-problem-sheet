#!/usr/bin/python

weight = int(input("\nEnter weight: "))

height = ( int(input("\nEnter height: ")) / 100 ) ** 2

print('\n BMI is', round(weight/height,1),' \n')