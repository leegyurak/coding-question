def solution(s):
    answer_list = []

    s_list = s.split(' ') #1

    for s_word in s_list: #2
        s_new_word = ''
        
        for idx, s_element in enumerate(s_word): #3
            if idx % 2 == 0: #4
                s_new_word += s_element.upper()
            else:
                s_new_word += s_element.lower()
        answer_list.append(s_new_word)

    answer = ' '.join(answer_list) #5
            
    return answer