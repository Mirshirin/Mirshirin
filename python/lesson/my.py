#import sys
#from enum import Enum
# print("❤😁🤦‍♀️  ")
# print("❤😁🤦‍♀️  ")
# print("❤😁🤦‍♀️  ")
# print("❤😁🤦‍♀️  ")
# print("❤😁🤦‍♀️  ")
# a= input('your number: ')
# p=int(a)
# print(" your num is  ", p)
# def h():
#     print("hek")

# h()
num=0
total=0
def addnum(num):
    if (num>=9):        
        return num + 1

    total = num + 1
    print(total)

    return addnum(total)


new = addnum(0)
print(new)
#sys.exit
