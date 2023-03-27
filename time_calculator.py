def add_time(start, duration):
    
    return_time = ''

    start_time_split = start.split(' ')
    start_hours = int(start_time_split[0].split(':')[0])
    start_minutes = int(start_time_split[0].split(':')[1])
    am_pm = start_time_split[1]

    print(start_hours)
    print(start_minutes)
    print(am_pm)

    return return_time

    # TODO
    
    return new_time
