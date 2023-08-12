        
def int32(x):
    if x>0xFFFFFFFF:
        raise OverflowError
    if x>0x7FFFFFFF:
        x=int(0x100000000-x)
        if x<2147483648:
            return -x
        else:
            return -2147483648
    return x

def solution(l):
    count = 0
    loop = 0
    for i, x in enumerate(l):
        for j, y in enumerate(l[i+1:]):  
            loop +=1 
            if y % x == 0:              #x divides y
                loop -= 1
                for z in l[i+j+2:]:
                    loop +=1
                    if z % y == 0:      #y divides z
                        print(x,y,z)
                        count +=1
    print(loop)
    return int32(count)


arr = [2,3,4,5,6,7,8,9,12, 16,24,47834728,2343,274,12312323,283729487329847234,32492378472394,3423974892374]
print(solution(arr))
