# # {
# # :{"math": 36, "science": 80, "english": 90},
# # 2:{"math": 36, "science": 80, "english": 90},
# # 3:{"math": 12, "science": 10, "english": 5},
# # 4:{"math": 92, "science": 54, "english": 80},
# # 5:{"math": 54, "science": 90, "english": 90},
# # }

# def grade(score):
#     if score >= 90:
#         return 'A'
#     elif 80 <= score < 90:
#         return 'B'
#     elif 70 <= score < 80:
#         return 'C'
#     elif 60 <= score < 70:
#         return 'D'
#     else:
#         return 'F'

# student_scores = {
#     1: {"math": 36, "science": 80, "english": 90},
#     2: {"math": 36, "science": 80, "english": 90},
#     3: {"math": 12, "science": 10, "english": 5},
#     4: {"math": 92, "science": 54, "english": 80},
#     5: {"math": 54, "science": 90, "english": 90},
# }



# for student_id, score in student_scores.items():
#     total= sum(score.values())
#     average_grade= total/len(score)
#     get_marks= grade(average_grade)
#     print(get_marks)

#     print(score)
#     print(average_grade)
# # print(get_marks)

# #def name(*args, **kwargs) gives unlimited values in function like name(1,2,3,4 which are *args and **kwargs gives key arg such as a=b or c=d)


# def unlimited(*args, **kwargs):

#     # print(args)
#     return args
# a= int(input("Enter the number"))
# b= int(input("Enter the number"))
# c= int(input("Enter the number"))  

# d= unlimited(a,b,c)
# print(d)

# def add(a, b= None):
#      print(a+b)
# add(a=1)

# def calculator(*agrs):
#     sum = 0
#     for i in agrs:
#         sum += i 
#     return sum
# a= int(input("enter your number"))
# b= int(input("enter your number"))
# c= int(input("enter your number"))



# def add(a,b): #hi indicate the name that we have in return
#     return a+b
# c= add(2,3)
# d= add("abcd","efgh")
# print(c)
# print(d)

# Create a function that reverses a given list.

# def Puja(number):
#     n = len(number)
#     reversed_list = []
#     for i in range(n - 1, -1, -1):
#         reversed_list.append(number[i])
#     return reversed_list

# # Example usage (same as before)
# original_list = [1, 2, 3, 4, 5]
# reversed_list = Puja(original_list)

# print(original_list)
# print(reversed_list)



def Reverse(number):
    length = len(number)
    reversed_list = []
    for i in range(length-1, -1, -1):
        reversed_list.append(number[i])
    return reversed_list 

og_list = [1,2,3,4]
reversed_list= Reverse(og_list)
print(og_list)
print(reversed_list) 


# Write a function that takes a list as input and returns a new list containing only unique elements.
# Implement a function that capitalizes the first letter of each word in a given string.
# Write a function that uses list comprehension to generate a list of squares of the numbers from 1 to n.
# Write a function to transpose a given matrix (swap rows with columns).




    