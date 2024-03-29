'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.
'''
import math

height = float(input('1Enter your height in meters \n'))
weight = float(input('Enter your weight in kgs \n'))
bmi = float(weight)/math.pow(float(height),2)

if bmi>35:
    print("You're clinically obese")
elif 30<bmi<=35:
    print("You're Obese")
elif 25<bmi<=30:
    print("You're slightly overweight")
elif 18.5<bmi<=25:
    print("You've normal weight")
else:
    print("You're underweight")
