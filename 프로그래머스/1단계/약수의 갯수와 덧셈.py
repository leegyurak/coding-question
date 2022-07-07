def solution(left, right):
    answer = 0

    for i in range(left, right + 1): #1
        cnt = 0

        for j in range(1, int(i/2) + 1): #2
            if i % j == 0: #3
                cnt += 1
        cnt += 1 #4

        if cnt % 2 == 0: #5
            answer += i
        else:
            answer -= i
            
    return answer