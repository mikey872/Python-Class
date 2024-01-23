# Square each element in a list:
# Write a Python program that takes a list of numbers and uses a lambda function to square each element in the list. Print both the original list and the list of squared numbers.

# anjal = [1,2,3,4]
# b = list(map(lambda  x:x **2, anjal))
# print(b)

#  Find the cube of odd numbers:
# Write a Python program that takes a list of numbers and uses a lambda function to filter out the odd numbers and then cubes each of the odd numbers. Print both the original list and the list of cubed odd numbers.

# number = [1,2,3,4,5,6]
# b = list(filter(lambda x:x%2 != 0,map(lambda x:x**3, number)))
# print(b)


# Calculate the sum of two lists:
# Write a Python program that takes two lists of numbers and uses a lambda function to calculate the sum of corresponding elements from both lists. Print both the lists and the resulting list of sums.  

# num1= [1,2,3,4,5]
# num2= [1,2,3,4,5]
# sum= list(map(lambda x,y:x+y, num1,num2))
# print(sum)


fibonacci = lambda n: n if n <=1 else fibonacci(n - 1) + fibonacci(n - 2)
for i in range(10):
    print(fibonacci(i))

    0,1,2,3,4,5,6,7,8,9,10
