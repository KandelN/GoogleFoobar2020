def solution(M, F):
    m, f = int(M), int(F)
    gen = 0
    while True:
        print((m,f))
        if m == f:
            if m == 1:
                return(str(gen))
            else:
                return("impossible")
                        
        if m < f:
            m, f = f, m
        
        rem = m // f
        
        m = ( m - rem * f )
        if m == 0:
            m += f
            rem -= 1
        gen += rem


print(solution(input(""), input("")) )