#function for sorting list items in ascending order
def sortasc(numbers):
    num=numbers
    n=len(num)
    sorted = []
    for i in range(n):
        min = num[0]
        for j in range(len(num)):
            if num[j]<min:
                min=num[j]
        sorted.append(min)
        num.remove(min)

    return sorted

#function for sorting list items in descending order:
def sortdesc(numbers):
    num= numbers
    n=len(num)
    sorted=[]
    for i in range(n):
        max=num[0]
        for j in range(len(num)):
            if num[j]>max:
                max=num[j]
        sorted.append(max)
        num.remove(max)

    return sorted    
