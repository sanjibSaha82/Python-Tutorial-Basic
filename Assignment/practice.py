# name = "Attugra"
# age = 7
# city = "Kolkata" 
# print("My name is", name, "from", city, "& I'm", age )

# print(f"My name is {name} from {city} & I'm {age}")

# a = 5 
# b = 3

# print(a == b)   # equal operator 
# print(a != b)   # not equal operator

# a = 10 
# b = 20
# print(a>10 and b<10) # and operator
# print(a==10 and b==20)
# print(a==10 or b<10) # or operator

# score = 85
# if score >= 90:

#      print("Grade - A")
# elif score >= 80: 
#      print("Grade - B")
# elif score >= 70: 
#      print("Grade - C")
# elif score >= 60:
#         print("Grade - D")
# else:
#    print("Grade - E")


year = int(input("Enter a Year (e.g. 2026): "))

# checking leap year
if (year % 4 == 0) or (year % 400 == 0):
    print(f"{year} is leap year") 
else:
    print(f"{year} is not leap year")




