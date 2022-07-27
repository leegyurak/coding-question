def solution(a, b):
    day = 0 #1
    day_of_the_week_list = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'] 

    month_day_list = [ #2
        [1, 31],
        [2, 29],
        [3, 31],
        [4, 30],
        [5, 31],
        [6, 30],
        [7, 31],
        [8, 31],
        [9, 30],
        [10, 31],
        [11, 30],
        [12, 31]
    ]

    for month_day in month_day_list: #3
        if a == month_day[0]:
            day += b
            break
        else:
            day += month_day[1]

    day_of_the_week_idx = day % 7 - 1 #4
            
    return day_of_the_week_list[day_of_the_week_idx]