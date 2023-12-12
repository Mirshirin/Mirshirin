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

