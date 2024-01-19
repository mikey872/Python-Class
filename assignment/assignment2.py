# Write a function called calculate_area that takes two positional arguments, length and width, and returns the area of a rectangle. Test the function with different values for length and width.

# def calculate_area(l,b):
#     area= length*breadth
#     return area
# length= int(input("Enter the number: "))
# breadth= int(input("Enter the width: "))
# result = calculate_area(length,breadth)
# print("The area of rectanlge: ",result)



# Create a function named print_info that takes three keyword arguments: name, age, and city. The function should print a sentence like "John is 25 years old and lives in Cityville." Test the function by passing values for each keyword argument

# def print_info(name,age,city):
#     sentence= (f"{name} is {age} years old and lives in {city}.")
#     # print(f"{name} is {age} years old and lives in {city}.")
#     print(sentence)
# Name = "John"
# Age= 25
# City = "Cityville"
# result = print_info(Name,Age,City)
# print(result)


# Define a function called power that takes two arguments, base and exponent, with a default value of 2 for the exponent. The function should return the result of raising the base to the given exponent. Test the function with different values for the base and exponent.
# Mix of Positional and Default Arguments:

def power(base,exponent=2):
    return base ** exponent
base1 = (3)
result = power(base1) 
print(result)

# Write a function named greet_user that takes a positional argument name and a default argument greeting with a default value of "Hello". The function should return a greeting message using the provided name and greeting. Test the function with different names and, optionally, provide a custom greeting for some cases.

# def greet_user(name, greeting="Hello"):
#     sentence = (f"{greeting},{name}")
#     print(sentence)
# user=input("Enter your Name: ")
# result = greet_user(user) 


# Define a function called calculate_sum that can take an arbitrary number of arguments and returns their sum. Test the function with different numbers of arguments, both positional and keyword.

# def calculate_sum(*agrs):
#     return sum(agrs)
# one = calculate_sum(1, 2, 3)
# print(one)