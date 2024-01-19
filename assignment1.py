Number_list= []
def calculator():
    while True:
        user= input("Enter the number and type N to end the ")
        if user=="n":
            break
        elif not user.isdigit():
            print("please give the integer")
        else:
            print("executed here")
            # continue
            number = int(user)
            Number_list.append(number)
    # return Number_list
calculator()

print(Number_list)



