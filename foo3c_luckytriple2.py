def solution(l):
    arr = []    
    loop = 0
    for i in range(len(l)):
        verify = 0
        count = 0
        for j in range(i):
            if l[i] % l[j] == 0:
                verify += 1
                count += arr[j][0]
            loop +=1
        print(l[i], verify, count)            
        arr.append((verify, count))  
    #new = list(filter(lambda a: a != 0, arr[1]))
    #counter = sum(new) - len(new)
   # print(count)
    counter = sum([x[1] for x in arr])
    print("LOOPS: ", loop)
    return counter
            






arr = [2,3,4,5,6,7,8,9,12, 16,24,47834728,2343,274,12312323,283729487329847234,32492378472394,3423974892374]
arr2 = [2,3,4,5,6,7,8,9,12,16,24]
print(solution(arr))
