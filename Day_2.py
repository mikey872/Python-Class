# write a fuction that uses list comprehension to generate a list of squares of the number from 1 to n

# nnumber=int(input("Enter the number"))

# def generate_square(number):
#     return number **2
# def generate_list_of_number(*args):
#     print(args)
    
    # for i in args:
    #     print(i)
    #     print(generate_square(i))
    # return [generate_square(i) for i in args]


# number_ = range(1, nnumber+1)
# result = generate_list_of_number(*number_)
# print(result)

user = int(input("Enter the number: "))
def square(number):
    return number **2
def list_of_number(*args):
    print(args)
    for i in args:
        print(i)
        print(square(i))
input = range(1, user+1)
result = list_of_number(*input)
# print(result)





