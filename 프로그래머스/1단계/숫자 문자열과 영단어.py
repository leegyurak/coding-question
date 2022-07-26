def solution(s):
    num_dict = { #1
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    answer = ''
    eng_num = ''

    for element in s:
        if element.isdigit(): #2
            answer += element
        else: 
            eng_num += element #3

            if num_dict.get(eng_num) is not None: #4
                answer += str(num_dict.get(eng_num))
                eng_num = ''
                
    return int(answer)