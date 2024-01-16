#try and except

# a=12
# b=12

# class Invalidinput(Exception):
#     pass
# try:
#     c= a/b
#     raise Invalidinput("Input is invalid")
#     print(a/b*c)
# except(TypeError, ZeroDivisionError, TypeError, Invalidinput) as e: #shortform to indicate all the exception you have made
#     print("hi")
# else:
#     print(c)
# finally:
#     print("ok")

a = [1,2,3]
try:
    b= a[3]
    print(b)
except(IndexError):
    print("invalid number")
else:
    print(a)
print('helo')
