
def solution(total_lambda):
    N =total_lambda
    if N == 1:
        return 0

    #fibonacci
    a = 1
    b = 1
    sum = 2
    counter1 = 2
    while (sum <= N):
        c = a+b
        sum += c
        counter1 += 1
        a = b
        b = c
    counter1 -= 1

    #doubles
    a = 1
    sum = 0
    counter2 = 0
    while (sum <= N):
        sum += a
        counter2 += 1
        a = 2*a
    counter2 -=1

    return (counter1 - counter2)


print(solution(int(input(""))))