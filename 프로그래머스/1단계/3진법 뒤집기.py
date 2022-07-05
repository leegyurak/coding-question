three_notation_elements = []

def three_notation(n): #1
    three_notation_elements.append(str(n%3))
    n = int(n/3)

    if n == 0:
        return
    else:
        three_notation(n)

def solution(n):
    three_notation(n)

    three_notation_str = ''.join(three_notation_elements) #2
    three_notation_str = str(int(three_notation_str)) #3

    answer = int(three_notation_str, 3) #4
    return answer
