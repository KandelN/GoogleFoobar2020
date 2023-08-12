def solution(string):
    string = string.lower()
    length = len(string)
    factors = []
    for i in range(1,length,1):
        if length%i == 0:
            factors.append(i)
    factors.append(length)

    for n in factors:
        #initializing empty list 
        groups = []
        t = 0
        while (t < length):
            group = string[t: t + n]
            groups.append(group)
            t = t + n

        if len(set(groups)) == 1:
            return len(groups)

print(solution(input("")))
