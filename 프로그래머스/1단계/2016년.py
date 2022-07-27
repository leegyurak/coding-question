def solution(a, b):
    day_of_the_week_list = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'] #1
    day_of_the_week_idx = 0

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

    day = 0

    for month_day in month_day_list: #3
        if a == month_day[0]:
            day += b
            break
        else:
            day += month_day[1]

    while True: #4
        day %= 7

        if day < 7:
            day_of_the_week_idx = day - 1
            break
            
    return day_of_the_week_list[day_of_the_week_idx]