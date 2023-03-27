def add_time(start, duration, weekday=False):

    return_time = ''

    start_time_split = start.split(' ')
    start_hours = int(start_time_split[0].split(':')[0])
    start_minutes = int(start_time_split[0].split(':')[1])
    am_pm = start_time_split[1]

    print(start_hours)
    print(start_minutes)
    print(am_pm)

    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])

    print(duration_hours)
    print(duration_minutes)
    
    # TODO

    return return_time
