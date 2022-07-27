def solution(n):
    add_num = 0 #1
    answer = 0
    
    for i in range(1, n+1): #2
        for j in range(i, n + 1): #3
            add_num += j

            if add_num == n: #4
                answer += 1
                add_num = 0
                break
            elif add_num > n:
                add_num = 0
                break
                
    return answer