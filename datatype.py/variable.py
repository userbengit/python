CURRENT_YEAR = 2021
 firstname = input("")
firstname = str(firstname)
lastname = input()
year_born = input()
year_born = int(year_born)
age = CURRENT_YEAR - year_born
height_meter = input()
height_meter = float(height_meter)
height_feet = height_meter * 3.281
height_feet = round(height_feet,1)

print("Your name is " + firstname + " " + lastname)
print("When you were born :")
print("You are" + str(age) + "years old in " + str(CURRENT_YEAR))
print("Your height (meter) :")
print("You are" +str(height_feet) + "feet tall")