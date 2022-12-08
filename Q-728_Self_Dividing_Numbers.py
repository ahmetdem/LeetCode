left = 5
right = 100

sequence = list(range(left, right))

def getDig(num):
    diglist = []
    
    while num > 0:
        lastDig = num % 10
        diglist.append(lastDig)
        num //= 10
    
    return diglist

def isSelf(num):
    digitlist = getDig(num)

    if 0 in digitlist:
        return False
    
    for i in digitlist:
        if num % i != 0:
            break
    else: return True 
    

answer = list(filter(isSelf, sequence))

print(answer)    