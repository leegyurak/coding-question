def solution(nums):
    answer = 0
    remove_overlap_nums = list(set(nums)) #1
    answer = len(remove_overlap_nums) #2
    if answer > int(len(nums) / 2): #3
        answer = int(len(nums) / 2) #4
    return answer